from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()

class Book(models.Model):
    title = models.CharField()
    author = models.Foreignkey(author, on_delete = models.CASCADE, name= 'writer')
    return self.name
    
class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book, related_name ='library')

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete=model.CASCADE)

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