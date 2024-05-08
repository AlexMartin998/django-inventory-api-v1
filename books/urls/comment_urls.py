from django.urls import path

from books.views.comment_views import (
    CommentView,
    CommentDetailView,
)


urlpatterns = [
    path("", CommentView.as_view(), name="comment"),
    path("<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
