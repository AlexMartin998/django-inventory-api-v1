from django.urls import path

from books.views.alex_views import (
    AlexView,
    AlexDetailView,
)


urlpatterns = [
    path("", AlexView.as_view(), name="alex"),
    path("<int:pk>/", AlexDetailView.as_view(), name="alex-detail"),
]
