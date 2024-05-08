from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.aba_model import Aba


# ### Aba Serializer - Model ===============
class AbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aba
        fields = '__all__'


# ## Response: Get All & Get By ID
class AbaResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aba
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class AbaFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aba
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class AbaOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Aba
        fields = '__all__'


# ## Get All Response
class AbaQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = AbaResponseSerializer(many=True, required=False)
