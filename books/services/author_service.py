from backend.shared.services.base_service import BaseService

from books.repositories.author_repository import AuthorRepository
from books.filters.author_filters import AuthorFilter
from books.serializers.author_serializers import (
    AuthorSerializer,
    AuthorResponseSerializer,
)


class AuthorService(BaseService):
    filter = AuthorFilter

    serializer = AuthorSerializer
    serializer2 = AuthorResponseSerializer

    def __init__(self, repository: AuthorRepository):
        super().__init__(repository)
