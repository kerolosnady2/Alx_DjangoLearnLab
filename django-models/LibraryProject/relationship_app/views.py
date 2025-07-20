from django.views.generic import DetailView
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Make sure this template exists
    context_object_name = "library"

# Register
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# List Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

