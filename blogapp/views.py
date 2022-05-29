from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from .forms import BlogForm, BlogModelForm
from django.utils import timezone

def home(req):
    # 블로그 글들을 모조리 띄우는 코드
    # queryset = Blog.objects.all()
    queryset = Blog.objects.filter().order_by("date")
    return render(req, 'index.html', {'posts':queryset})

# 블로그 글 작성하는 html 보여주는 함수(html form에 대한 get 함수)
def new(req):
    return render(req, 'html_form.html')

def detail(req, blog_id):
    # queryset = Blog.objects.filter(id=blog_id) --> 이렇게 하면 안 됨
    queryset = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'detail.html', {"blog_detail":queryset})

# 블로그 글 저장하는 함수(html form에 대한 post 함수)
def html_form(req):
    if req.method == 'POST':
        post = Blog()
        post.title = req.POST['title']
        post.body = req.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form에 대한 get, post 두 요청 모두 처리 가능한 함수
def django_form(req):
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
        return render(req, 'django_form.html', {'form':form})

# django model form
def djangomodel_form(req):
    if req.method == 'POST' or req.method =='FILES':
        form = BlogModelForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
        return render(req, 'django_form.html', {'form':form})
