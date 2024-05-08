from django.urls import path

from books.views.aba_views import (
    AbaView,
    AbaDetailView,
)


urlpatterns = [
    path("", AbaView.as_view(), name="aba"),
    path("<int:pk>/", AbaDetailView.as_view(), name="aba-detail"),
]
