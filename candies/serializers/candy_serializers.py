from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from candies.models.candy_model import Candy


# ### Candy Serializer - Model ===============
class CandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = '__all__'


# ## Response: Get All & Get By ID
class CandyResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Candy
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class CandyFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Candy
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class CandyOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Candy
        fields = '__all__'


# ## Get All Response
class CandyQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = CandyResponseSerializer(many=True, required=False)
