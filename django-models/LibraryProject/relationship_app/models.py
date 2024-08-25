from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, name= 'writer')
    class Meta: 
         permissions = [('can_add_book, Can add Book'), ('can_change_book, Can change book'), ('can_delete_book, Can delete book')]

    
class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book, related_name ='library')

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = ('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')
    role = models.CharField(max_length=20, choices = ROLE_CHOICES)

    def _str_(self):
        return f"{self.user.username} - {self.role}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = ('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')
    role = models.CharField(max_length=20, choices = ROLE_CHOICES)

    def _str_(self):
        return f"{self.user.username} - {self.role}"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()