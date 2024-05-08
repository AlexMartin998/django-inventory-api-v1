from django.urls import path

from books.views.aaran_views import (
    AaranView,
    AaranDetailView,
)


urlpatterns = [
    path("", AaranView.as_view(), name="aaran"),
    path("<int:pk>/", AaranDetailView.as_view(), name="aaran-detail"),
]
