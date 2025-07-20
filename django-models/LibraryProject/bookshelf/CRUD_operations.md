# CRUD Operations

## Create
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# <Book: 1984>

