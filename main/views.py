from django.shortcuts import render
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from authentication.models import User
@login_required(login_url='/')
def main(request):
    
    categories = Category.objects.all()
    posts = Post.objects.all()  
    context = {
        'categories': categories,
        'posts': posts
    }
    
    return render(request, 'main.html', context)


@login_required(login_url='/')
def post_detail(request, pk):
    
    categori = Category.objects.get(id=pk)
    categories = Category.objects.all()
    posts = Post.objects.filter(category=categori)   
    
    context = {
        'categories': categories,
        'posts': posts,
        'categori': categori
    }
     
    return render(request, 'post_detail.html', context)
