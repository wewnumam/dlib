from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

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

def signup(request):
    context = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
    return render(request,'home/signup.html',
                          {'user_form':user_form,
                           'registered':registered})