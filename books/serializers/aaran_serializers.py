from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.aaran_model import Aaran


# ### Aaran Serializer - Model ===============
class AaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aaran
        fields = '__all__'


# ## Response: Get All & Get By ID
class AaranResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aaran
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class AaranFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aaran
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class AaranOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aaran
        fields = '__all__'


# ## Get All Response
class AaranQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = AaranResponseSerializer(many=True, required=False)
