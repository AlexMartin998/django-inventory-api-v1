from backend.shared.filters.filters import BaseFilter
from books.models.aba_model import Aba


class AbaFilter(BaseFilter):
    class Meta:
        model = Aba
        fields = '__all__'
