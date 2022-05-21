from django.shortcuts import redirect, render
from .models import Blog
from .forms import BlogForm
from django.utils import timezone

def home(req):
    return render(req, 'index.html')

# 블로그 글 작성하는 html 보여주는 함수(html form에 대한 get 함수)
def new(req):
    return render(req, 'new.html')

# 블로그 글 저장하는 함수(html form에 대한 post 함수)
def create(req):
    if req.method == 'POST':
        post = Blog()
        post.title = req.POST['title']
        post.body = req.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form에 대한 get, post 두 요청 모두 처리 가능한 함수
def formcreate(req):
    if req.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(req.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력 받을 수 있는 html 가져다주기
        form = BlogForm
        return render(req, 'form_create.html', {'form':form})