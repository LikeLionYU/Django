from django.shortcuts import render

def login(req):
    return render(req, 'login.html')

def signup(req):
    return render(req, 'signup.html')