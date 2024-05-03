from backend.shared.filters import BaseFilter
from products.models.category_model import Category


class CategoryFilter(BaseFilter):
    class Meta:
        model = Category
        fields = "__all__"
        # fields = []

