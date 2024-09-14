from django.db import models
from datetime import datetime
from api.models import User

class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=CASCADE, name = 'product')
