from backend.shared.filters.filters import BaseFilter
from products.models.subcategory_model import SubCategory


class SubcategoryFilter(BaseFilter):
    class Meta:
        model = SubCategory
        fields = "__all__"
