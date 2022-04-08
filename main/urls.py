from django.urls import path
from .views import post_detail, main

urlpatterns = [
    # path('', main, name='main'),
    path('<int:pk>', post_detail, name='post_detail')
]