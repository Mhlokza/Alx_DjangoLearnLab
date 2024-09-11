from rest_framework.generics import(ListAPIView, DetailAPIView, CreateAPIView, UpdateAPIView, DeleteAPIView)
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated

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



class CreateView(CreateView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
