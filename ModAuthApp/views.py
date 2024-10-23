from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    pass

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('add_borrow_book')
    if request.user.is_authenticated:
        return redirect('add_borrow_book')
    messages.info(request, 'Please login')
    return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request,'You have log out successfully.')
    return redirect('signin')