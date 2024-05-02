from django.urls import path

from products.views.subcategory_view import SubcategoryView, SubcategoryDetailView


urlpatterns = [
    path('', SubcategoryView.as_view(), name='subcategory'),
    path('<int:id>/', SubcategoryDetailView.as_view(), name='subcategory-detail'),
]

