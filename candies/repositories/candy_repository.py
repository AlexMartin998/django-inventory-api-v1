from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from candies.models.candy_model import Candy


class CandyRepository(BaseRepository):
    model: Type[Candy]

    def __init__(self, model):
        super().__init__(model)
