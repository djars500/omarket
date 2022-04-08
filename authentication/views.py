from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as signin
from django.contrib.auth.decorators import login_required


def login(request):
    
    if request.user.is_authenticated:
        return redirect('posts/1')
    else:
    
        email = request.GET.get('email')
        password = request.GET.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            signin(request, user)
            return redirect('posts/1')
        else:
            print('ni')
            # return redirect('posts/')
        return render(request, 'signin.html')
    
