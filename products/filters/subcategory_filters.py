from backend.shared.filters.filters import BaseFilter
from products.models.category_model import Category


class SubcategoryFilter(BaseFilter):
    class Meta:
        model = Category
        fields = "__all__"
