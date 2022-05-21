from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone

def home(req):
    return render(req, 'index.html')

# 블로그 글 작성하는 html 보여주는 함수
def new(req):
    return render(req, 'new.html')

# 블로그 글 저장하는 함수
def create(req):
    if req.method == 'POST':
        post = Blog()
        post.title = req.POST['title']
        post.body = req.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')