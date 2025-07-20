# Delete

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by checking that no books remain
print(Book.objects.all())
# <QuerySet []>
