from django.urls import path
from .views import category_detail, main

urlpatterns = [
    path('', main, name='main'),
    path('category/<int:pk>/', category_detail, name='category')
]