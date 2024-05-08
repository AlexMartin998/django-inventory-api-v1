from backend.shared.services.base_service import BaseService

from books.repositories.aaran_repository import AaranRepository
from books.filters.aaran_filters import AaranFilter
from books.serializers.aaran_serializers import (
    AaranSerializer,
    AaranResponseSerializer,
)


class AaranService(BaseService):
    repository: AaranRepository

    filter = AaranFilter

    serializer = AaranSerializer
    serializer2 = AaranResponseSerializer

    def __init__(self, repository):
        super().__init__(repository)
