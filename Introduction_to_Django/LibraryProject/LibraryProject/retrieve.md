
### retrieve.md

```md
## Retrieve Book

```python
from bookshelf.models import Book
b = Book.objects.first()
b.title, b.author, b.publication_year
