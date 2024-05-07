from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.author_model import Author


# ### Author Serializer - Model ===============
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# ## Response: Get All & Get By ID
class AuthorResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class AuthorFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class AuthorOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# ## Get All Response
class AuthorQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = AuthorResponseSerializer(many=True, required=False)
