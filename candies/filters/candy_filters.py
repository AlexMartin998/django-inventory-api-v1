from backend.shared.filters.filters import BaseFilter
from candies.models.candy_model import Candy


class CandyFilter(BaseFilter):
    class Meta:
        model = Candy
        fields = '__all__'
