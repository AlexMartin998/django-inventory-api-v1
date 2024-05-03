from rest_framework import serializers

from backend.shared.serializers.serializers import FiltersBaseSerializer
from products.models.subcategory_model import SubCategory


# ### Subcategory =================================
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class SubcategoryFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

