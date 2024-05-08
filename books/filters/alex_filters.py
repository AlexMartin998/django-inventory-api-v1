from backend.shared.filters.filters import BaseFilter
from books.models.alex_model import Alex


class AlexFilter(BaseFilter):
    class Meta:
        model = Alex
        fields = '__all__'
