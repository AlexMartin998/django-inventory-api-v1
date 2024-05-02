from rest_framework import serializers

from backend.serializers import FiltersBaseSerializer
from products.models import Category, SubCategory


# ### Category =================================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Filter Serializer: all is optional thanks to FiltersBaseSerializer
class CategoryFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ### Subcategory =================================
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class SubcategoryFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

