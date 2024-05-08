from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from books.models.aaran_model import Aaran


class AaranRepository(BaseRepository):
    model: Type[Aaran]

    def __init__(self, model):
        super().__init__(model)
