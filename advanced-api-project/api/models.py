from django.db import models
#authors model that carries the information about the author
class Author(models.Model):
    name = models.CharField(max_length=100)
#each book writen by the author
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name ='product')
