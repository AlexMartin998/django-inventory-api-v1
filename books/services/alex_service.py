from backend.shared.services.base_service import BaseService

from books.repositories.alex_repository import AlexRepository
from books.filters.alex_filters import AlexFilter
from books.serializers.alex_serializers import (
    AlexSerializer,
    AlexResponseSerializer,
)


class AlexService(BaseService):
    repository: AlexRepository

    filter = AlexFilter

    serializer = AlexSerializer
    serializer2 = AlexResponseSerializer

    def __init__(self, repository):
        super().__init__(repository)
