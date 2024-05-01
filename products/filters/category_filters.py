import django_filters
from products.models import Category

class CategoryFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_fields = self.Meta.model._meta.fields
        for field in model_fields:
            if hasattr(field, 'name'):
                field_name = field.name
                self.filters[field_name] = django_filters.CharFilter(
                    field_name=field_name,
                    lookup_expr='icontains'
                )

    class Meta:
        model = Category
        fields = "__all__"
        # fields = []

