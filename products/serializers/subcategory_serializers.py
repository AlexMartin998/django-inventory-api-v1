from rest_framework import serializers

from backend.shared.serializers.serializers import FiltersBaseSerializer, OptionalFieldsModelSerializer
from products.models.subcategory_model import SubCategory



class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class SubcategoryFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'



# ## Swagger
class SubcategoryBodyDocSerializer(OptionalFieldsModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class SubcategoryResDocSerializer(OptionalFieldsModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class SubcategoryQueryDocSerializer(OptionalFieldsModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

