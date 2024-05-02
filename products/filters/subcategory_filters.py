from backend.shared.filters import BaseFilter
from products.models import Category


class SubcategoryFilter(BaseFilter):
    class Meta:
        model = Category
        fields = "__all__"
