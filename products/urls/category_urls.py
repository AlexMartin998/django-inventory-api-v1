from django.urls import path

# custom dirs deben tener un __init__.py
from ..views import category_view

urlpatterns = [

    path('', category_view.get_categories),
    path('<int:id>/', category_view.get_category),
    path('create/', category_view.create_category),
    path('update/<int:id>/', category_view.update_category),
    path('delete/<int:id>/', category_view.delete_category),

]
