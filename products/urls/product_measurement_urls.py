from django.urls import path

from products.views.product_measurement_view import (
    ProductMeasurementDetailView,
    ProductMeasurementView,
)


urlpatterns = [
    path("", ProductMeasurementView.as_view(), name="product-measurement"),
    path(
        "<int:pk>/",
        ProductMeasurementDetailView.as_view(),
        name="product-measurement-detail",
    ),
]
