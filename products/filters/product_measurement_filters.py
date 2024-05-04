from backend.shared.filters.filters import BaseFilter
from products.models.product_measurement_model import ProductMeasurement


class ProductMeasurementFilter(BaseFilter):
    class Meta:
        model = ProductMeasurement
        fields = "__all__"
