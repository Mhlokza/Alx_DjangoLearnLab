from rest_framework.generics import(ListAPIView, DetailAPIView, CreateAPIView, UpdateAPIView, DeleteAPIView)
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated
from rest_framework import filters 
from .filters import BookFilter
from rest rest_framework import status
from django_filters import rest_framework
from rest_framework import generics


class  ListView(generics.ListAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    filters_backends = rest_framework.djangoFiltersBackend, filters.SearchFilter.OrderingFilters
    filterset_class = BookFilter # Use the BookFilter class for filtering.
    search_fields = ['title', 'author__name'] # Search fields for the SearchFilter.
    ordering_fields = ['title', 'publication_year'] # Ordering fields for the OrderingFilter.
    ordering = ['title'] # Default ordering by title.

class  CreateView(CreateAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer


class DetailView(DetailAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer



class  UpdateView(UpdateAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

     Overriding the update process for additional validation
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            publication_year = serializer.validated_data.get('publication_year')
            current_year = date.today().year
            if publication_year > current_year:
                return Response({"publication_year": "The publication date cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)

            # Save if validation passes.
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(DeleteAPIView):
     permission_classes = [IsAuthenticated, IsAdmin]
     queryset = Book.objects.all()
     serializer_class =BookSerializer



class CreateView(CreateView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            publication_year = serializer.validated_data.get('publication_year')
            
            current_year = date.today().year
            if publication_year > current_year:
                return Response({"publication_year": "The publication date cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
