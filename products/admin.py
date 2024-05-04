from django.contrib import admin

from products.models.category_model import Category
from products.models.subcategory_model import SubCategory
from products.models.product_model import Product
from products.models.review_model import Reviews


# ### Register your MODELS here (/admin) de Django
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Product)
admin.site.register(SubCategory)
