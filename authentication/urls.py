from django.urls import path
from .views import login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login),
    path('logout/', LogoutView.as_view(), name = 'logout')
]
