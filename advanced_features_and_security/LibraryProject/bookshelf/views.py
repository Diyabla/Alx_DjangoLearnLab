from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        year = request.POST['publication_year']
        Book.objects.create(title=title, author_id=author_id, publication_year=year)
        return redirect('book_list')
    return render(request, 'bookshelf/add_book.html')


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required

# List books safely
@login_required
def list_books(request):
    books = Book.objects.all()  # ORM safely queries DB
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Add book securely with CSRF protection
@login_required
@permission_required('bookshelf.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Example safe search view
@login_required
def search_books(request):
    query = request.GET.get('q', '')
    # ORM handles parameterization, preventing SQL injection
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})
