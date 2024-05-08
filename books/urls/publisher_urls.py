from django.urls import path

from books.views.publisher_views import (
    PublisherView,
    PublisherDetailView,
)


urlpatterns = [
    path("", PublisherView.as_view(), name="publisher"),
    path("<int:pk>/", PublisherDetailView.as_view(), name="publisher-detail"),
]
