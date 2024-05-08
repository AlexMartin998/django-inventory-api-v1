from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from books.models.alex_model import Alex


class AlexRepository(BaseRepository):
    model: Type[Alex]

    def __init__(self, model):
        super().__init__(model)
