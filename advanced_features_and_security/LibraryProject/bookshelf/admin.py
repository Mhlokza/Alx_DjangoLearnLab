from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as CustomUser
from .models import User
class UserAdmin(CustomUserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Book)
admin.ModelAdmin
list_filter, author, publication_year
search_fields, title
