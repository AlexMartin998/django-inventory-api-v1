from backend.shared.filters.filters import BaseFilter
from books.models.publisher_model import Publisher


class PublisherFilter(BaseFilter):
    class Meta:
        model = Publisher
        fields = '__all__'
