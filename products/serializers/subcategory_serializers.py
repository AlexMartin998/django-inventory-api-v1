from rest_framework import serializers

from backend.serializers import FiltersBaseSerializer
from products.models import SubCategory


# ### Subcategory =================================
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class SubcategoryFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

