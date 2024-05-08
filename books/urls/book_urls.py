from django.urls import path

from books.views.book_views import (
    BookView,
    BookDetailView,
)


urlpatterns = [
    path("", BookView.as_view(), name="book"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
