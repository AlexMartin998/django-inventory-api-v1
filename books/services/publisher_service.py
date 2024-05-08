from backend.shared.services.base_service import BaseService

from books.repositories.publisher_repository import PublisherRepository
from books.filters.publisher_filters import PublisherFilter
from books.serializers.publisher_serializers import (
    PublisherSerializer,
    PublisherResponseSerializer,
)


class PublisherService(BaseService):
    repository: PublisherRepository  # se usa la instancia

    filter = PublisherFilter

    serializer = PublisherSerializer
    serializer2 = PublisherResponseSerializer

    def __init__(self, repository):
        super().__init__(repository)

    def some_extra_method(self):
        self.repository.find_one()
