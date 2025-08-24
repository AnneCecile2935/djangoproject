from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages

def book_list(request):
    books = Book.objects.all()  # Récupère tous les livres de la base
    return render(request, 'books/list.html', {'books': books})

def home(request):
    return render(request, 'books/home.html')

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livre ajouté avec succès !')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
