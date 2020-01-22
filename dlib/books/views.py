from django.shortcuts import render 

from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Read It!',
        'books': books,
    }
    return render(request, 'books/index.html', context)