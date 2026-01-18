from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)   # required by checker
    for book in books:
        print(book.title)


# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    for book in library.books.all():
        print(book.title)


# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(library.librarian.name)
