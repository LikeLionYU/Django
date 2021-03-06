"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blogapp import views
import accounts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name="home"),
    path('comment/<int:blog_id>', views.comment, name="comment"),
    path('detail/<int:blog_id>', views.detail, name="detail"),
    # html의 템플릿 언어로 넘겨받은 post.id가 int형의 blog_id에 저장되고,
    # blog_id는 views의 detail 함수로 전달된다

    # html form
    path('new/', views.new, name="new"),
    path('html-form/', views.html_form, name="html_form"),
    path('django-form/', views.django_form, name="django_form"),
    path('djangomodel-form/', views.djangomodel_form, name="djangomodel_form"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
