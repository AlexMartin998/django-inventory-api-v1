from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from products.models.product_measurement_model import ProductMeasurement


# ### Product Measurement Serializer - Model ===============
class ProductMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMeasurement
        fields = "__all__"


# ### Filter Serializer - Get All ===============
class ProductMeasurementFilterSerializer(FiltersBaseSerializer):
    some_custom_filter = serializers.CharField(required=False)

    class Meta:
        model = ProductMeasurement
        fields = "__all__"


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class ProductMeasurementOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = ProductMeasurement
        fields = "__all__"


# ## Response: Get All & Get By ID
class ProductMeasurementResDocSerializer(FiltersBaseSerializer):
    some_custom_field = serializers.CharField(required=False)

    class Meta:
        model = ProductMeasurement
        fields = "__all__"


# ## Get All Response
class ProductMeasurementQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = ProductMeasurementResDocSerializer(many=True, required=False)
