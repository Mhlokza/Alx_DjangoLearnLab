from django.db import models
from django.contrib.auth.models import Permission

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
