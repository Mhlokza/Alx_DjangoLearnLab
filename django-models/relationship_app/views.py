from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
