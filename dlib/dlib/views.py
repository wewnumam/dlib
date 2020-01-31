from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Find Your World!'
    }
    return render(request, 'home/index.html', context)

def signin(request):
    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'home/login.html')

def signout(request):
    if request.method == "POST":
        if request.POST['logout'] == "Submit":
            logout(request)

        return redirect('/')

    return render(request, 'home/logout.html')