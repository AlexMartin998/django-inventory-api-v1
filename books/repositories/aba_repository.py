from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from books.models.aba_model import Aba


class AbaRepository(BaseRepository):
    model: Type[Aba]

    def __init__(self, model):
        super().__init__(model)
