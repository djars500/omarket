from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_active', 'is_omarket', 'is_wildberres', 'is_tender')
    list_filter = ('email', 'is_active', 'is_omarket', 'is_wildberres', 'is_tender')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'image','courses' )}),
        ('Permissions', {'fields': ('is_active', 'is_omarket', 'is_wildberres', 'is_tender')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'image','is_active', 'is_omarket', 'is_wildberres', 'is_tender')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)