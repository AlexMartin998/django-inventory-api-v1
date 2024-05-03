from rest_framework import serializers
from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from products.models.subcategory_model import SubCategory


# ### Subcategory Serializer - Model ===============
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


# ### Filter Serializer - Get All ===============
class SubcategoryFilterSerializer(FiltersBaseSerializer):
    some_custom_filter = serializers.CharField(required=False)

    class Meta:
        model = SubCategory
        fields = "__all__"


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class SubcategoryOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


# ## Response: Get All & Get By ID
class SubcategoryResDocSerializer(FiltersBaseSerializer):
    some_custom_field = serializers.CharField(required=False)

    class Meta:
        model = SubCategory
        fields = "__all__"


# ## Get All Response
class SubcategoryQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = SubcategoryResDocSerializer(many=True, required=False)
