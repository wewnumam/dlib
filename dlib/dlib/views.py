from django.shortcuts import render 

def index(request):
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Find Your World!'
    }
    return render(request, 'home/index.html', context)