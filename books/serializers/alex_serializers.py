from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.alex_model import Alex


# ### Alex Serializer - Model ===============
class AlexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alex
        fields = '__all__'


# ## Response: Get All & Get By ID
class AlexResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Alex
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class AlexFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Alex
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class AlexOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Alex
        fields = '__all__'


# ## Get All Response
class AlexQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = AlexResponseSerializer(many=True, required=False)
