from rest_framework import serializers

from backend.shared.serializers.serializers import (
    FiltersBaseSerializer,
    QueryDocWrapperSerializer,
)
from books.models.comment_model import Comment


# ### Comment Serializer - Model ===============
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ## Response: Get All & Get By ID
class CommentResponseSerializer(FiltersBaseSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ### Filter Serializer - Get All ===============
class CommentFilterSerializer(FiltersBaseSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ### Swagger ===============
# ## Response Body: Post & Put & Patch
class CommentOptDocSerializer(FiltersBaseSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ## Get All Response
class CommentQueryDocWrapperSerializer(QueryDocWrapperSerializer):
    data = CommentResponseSerializer(many=True, required=False)
