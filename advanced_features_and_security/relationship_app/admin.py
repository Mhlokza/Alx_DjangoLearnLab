from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import User

class UserAdmin(CustomUserAdmin):
    pass

admin.site.register(User, UserAdmin)

