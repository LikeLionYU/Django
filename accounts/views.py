from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(req, username=username, password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('home')
        else :
            return render(req,'login.html')
    else:
        return render(req,'login.html')

def logout(req):
    auth.logout(req)
    return redirect('home')

def signup(req):
    return render(req, 'signup.html')