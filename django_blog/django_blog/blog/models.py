from django.db import models
frome datetime import datetime
from advanced-api-project.api.models import User

class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=CASCATE, name = 'product')
    








    




