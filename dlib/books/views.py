from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Start Reading!',
        'books': books,
    }
    return render(request, 'books/index.html', context)

def detail(request, input):
    if request.user.is_authenticated:
        book = Book.objects.get(slug=input)
        context = {
            'title': book.title,
            'category': book.category,
            'writer': book.writer,
            'year': book.year,
            'synopsis': book.synopsis,
            'cover': book.cover,
            'filename': book.filename,
        }
        return render(request, 'books/detail.html', context)
    else:
        return redirect('/login')

def search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(Q(title__icontains=query) | Q(writer__icontains=query)| Q(synopsis__icontains=query))
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Search Result',
        'books': books,
    }
    return render(request, 'books/index.html', context)