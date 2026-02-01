from django.shortcuts import render
from .models import Book, Library , Author
from django.views.generic import DetailView

# Function-based view: lists all books


def list_books(request):
    books = Book.objects.all()   # fetch all books
    context = {'books': books}   # pass to template
    return render(request, 'relationship_app/list_books.html', context)



# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # name used in template to access library object
    
