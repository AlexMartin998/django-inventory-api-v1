from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.publisher_model import Publisher


# ### Publisher Serializer - Model ===============
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


# ## Response: Get All & Get By ID
class PublisherResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class PublisherFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class PublisherOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


# ## Get All Response
class PublisherQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = PublisherResponseSerializer(many=True, required=False)
