from backend.shared.filters.filters import BaseFilter
from books.models.author_model import Author


class AuthorFilter(BaseFilter):
    class Meta:
        model = Author
        fields = '__all__'
