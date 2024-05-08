from django.urls import path

from candies.views.candy_views import (
    CandyView,
    CandyDetailView,
)


urlpatterns = [
    path("", CandyView.as_view(), name="candy"),
    path("<int:pk>/", CandyDetailView.as_view(), name="candy-detail"),
]
