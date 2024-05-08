from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from books.models.publisher_model import Publisher


class PublisherRepository(BaseRepository):
    model: Type[Publisher]  # se usa la class

    def __init__(self):
        super().__init__(Publisher)

    def get_one(self, id):
        return self.model.objects.get(id=id)
