from django.db import models
from django.contrib.auth.models import Permission
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publication_year = models.IntegerField()

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False)
    profile_photo = models.ImageField()

class Permissions(models.Model):
    premissions = [('can_view', 'Can view'), ('can_create', 'Can view'),
                   ('can _edit', 'Can edit'), ('can_delete', 'Can delete')]

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise valuesError("user should have an email")
        user = self.model(email= self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user 

    
    def create_superuser(self,email,password):
        user = self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using =self._db)
        user.save()
# get permissions
permissions = Permission.objects.get(codename = 'can_view, can_create, can_edit, can_delete')
permission =Permission.objects.get(codename = 'can_view')
admin_perm = Permission.objects.get(codename = 'can_view, can_delete')
Editors.permissions.add(permissions)
Viewers.Permission.add(permission)
Admins.Permission.add(admin_perm)
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)