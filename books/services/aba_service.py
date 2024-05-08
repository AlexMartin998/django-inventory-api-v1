from backend.shared.services.base_service import BaseService

from books.repositories.aba_repository import AbaRepository
from books.filters.aba_filters import AbaFilter
from books.serializers.aba_serializers import (
    AbaSerializer,
    AbaResponseSerializer,
)


class AbaService(BaseService):
    repository: AbaRepository

    filter = AbaFilter

    serializer = AbaSerializer
    serializer2 = AbaResponseSerializer

    def __init__(self, repository):
        super().__init__(repository)
