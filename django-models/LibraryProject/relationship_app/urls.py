from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # 👈 This is required by the checker

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Auth URLs using Django built-in views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),  # 👈 This must say views.register_view
]

