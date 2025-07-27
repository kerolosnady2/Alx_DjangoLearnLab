from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in the admin list
    search_fields = ('title', 'author')                     # Enable search on title and author
    list_filter = ('publication_year',)                     # Enable filtering by publication year
