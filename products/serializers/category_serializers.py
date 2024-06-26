from rest_framework import serializers

from backend.shared.serializers.serializers import FiltersBaseSerializer
from products.models.category_model import Category


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
