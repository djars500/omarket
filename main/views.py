from django.shortcuts import render
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from authentication.models import User


def main(request):
    context  = {}
    if request.user.is_authenticated:
        categories = request.user.courses.all()
        context = {
            'categories': categories
        }
        
    
    
    return render(request, 'main-page.html', context)


@login_required(login_url='/')
def category_detail(request, pk):

    categories = request.user.courses.filter(id=pk)

    if len(categories) > 0:        
        posts = Post.objects.filter(category_id=pk).order_by('-id')
        print(posts)
        context = {
            "posts": posts,
            "category": categories[0]
        }   
        return render(request, 'category_detail.html', context)
    else:
        return render(request, 'not-found.html')

    
    
