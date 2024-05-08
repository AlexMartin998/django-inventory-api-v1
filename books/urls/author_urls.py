from django.urls import path

from books.views.author_views import (
    AuthorView,
    AuthorDetailView,
)


urlpatterns = [
    path("", AuthorView.as_view(), name="author"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]
