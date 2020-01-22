from django.shortcuts import render 

def index(request):
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Read It!'
    }
    return render(request, 'books/index.html', context)