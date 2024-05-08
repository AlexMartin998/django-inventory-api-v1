from typing import Type

from books.models.author_model import Author
from backend.shared.repositories.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    model: Type[Author]

    def __init__(self):
        super().__init__(Author)
