from backend.shared.services.base_service import BaseService

from books.repositories.comment_repository import CommentRepository
from books.filters.comment_filters import CommentFilter
from books.serializers.comment_serializers import (
    CommentSerializer,
    CommentResponseSerializer,
)


class CommentService(BaseService):
    filter = CommentFilter

    serializer = CommentSerializer
    serializer2 = CommentResponseSerializer

    def __init__(self, repository: CommentRepository):
        super().__init__(repository)
