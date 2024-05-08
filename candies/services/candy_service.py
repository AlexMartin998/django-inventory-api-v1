from backend.shared.services.base_service import BaseService

from candies.repositories.candy_repository import CandyRepository
from candies.filters.candy_filters import CandyFilter
from candies.serializers.candy_serializers import (
    CandySerializer,
    CandyResponseSerializer,
)


class CandyService(BaseService):
    repository: CandyRepository

    filter = CandyFilter

    serializer = CandySerializer
    serializer2 = CandyResponseSerializer

    def __init__(self, repository):
        super().__init__(repository)
