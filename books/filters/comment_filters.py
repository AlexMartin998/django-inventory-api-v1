from backend.shared.filters.filters import BaseFilter
from books.models.comment_model import Comment


class CommentFilter(BaseFilter):
    class Meta:
        model = Comment
        fields = '__all__'
