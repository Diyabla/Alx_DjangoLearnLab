# LibraryProject/bookshelf/views.py
# LibraryProject/bookshelf/views.py

from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, ExampleForm  # <-- Add ExampleForm here


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Example view for ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # You can process the form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # For example, just render a success page
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
