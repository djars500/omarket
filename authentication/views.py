from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as signin
from django.contrib.auth.decorators import login_required


def login(request):
    
    if request.user.is_authenticated:
        return redirect('posts/1')
    else:
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            signin(request, user)
            return redirect('/')
        else:
            print('ni')
        return render(request, 'login.html')
    
