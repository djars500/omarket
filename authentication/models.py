from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from main.models import Category
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_omarket = models.BooleanField(default=False)
    is_wildberres = models.BooleanField(default=False)
    is_tender = models.BooleanField(default=False)
    courses = models.ManyToManyField(Category)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email