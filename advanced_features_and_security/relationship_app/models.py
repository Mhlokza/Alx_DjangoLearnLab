from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, name= 'writer')
    def __str__(self):
        return self.name
    
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



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

#authethication
class User(AbstractUser):
    date_of_birth = models.DateField(max_length=20)
    profile_photo = models.ImageField()

class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise valuesError("user must have email")
        user = self.model(email= self.normalize_email(email))
        user.set_password(password)
        user.save(using= self._db)
        return user


    def create_superuser(self,email,password):
        user=self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth
    profile_photo

