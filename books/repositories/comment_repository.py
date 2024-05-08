from typing import Type

from backend.shared.repositories.base_repository import BaseRepository

from books.models.comment_model import Comment


class CommentRepository(BaseRepository):
    model: Type[Comment]

    def __init__(self):
        super().__init__(Comment)
