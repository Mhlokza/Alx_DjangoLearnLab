from django.urls import path
from .views import (ListView, DetailView, CreateView, UpdateView, DeleteView)


urlpatterns = [
    path('api/',ListView.as_view(),name='book-list')
    path('api/create',CreateView.as_view(),name='book-create')
    path('api/deatailed', DetailView.as_view(),name='book-detail')
    path('api/update',UpdateView.as_view(),name='book-update')
    path('api/delete'DeleteView.as_view(), name = 'book-delete')

    

] 