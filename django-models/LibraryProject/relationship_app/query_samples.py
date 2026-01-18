from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    for book in author.books.all():
        print(book.title)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    for book in library.books.all():
        print(book.title)

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(library.librarian.name)
