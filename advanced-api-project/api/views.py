from rest_framework.generics import(ListAPIView, DetailAPIView, CreateAPIView, UpdateAPIView, DeleteAPIView)
from .models import Book
from .serializers import BookSerializer

class  ListView(generics.ListAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

class  CreateView(CreateAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

class DetailView(DetailAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

class  UpdateView(UpdateAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer


