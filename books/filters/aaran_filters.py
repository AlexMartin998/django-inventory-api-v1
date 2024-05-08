from backend.shared.filters.filters import BaseFilter
from books.models.aaran_model import Aaran


class AaranFilter(BaseFilter):
    class Meta:
        model = Aaran
        fields = '__all__'
