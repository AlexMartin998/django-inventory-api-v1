from django.db import models

from backend.models import AuditDateModel
from users.models import User

from products.models.category_model import Category
from products.models.subcategory_model import SubCategory
from products.models.product_measurement_model import ProductMeasurement



# como AuditDateModel ya hereda de models.Model, no es necesario hacerlo en Product
class Product(AuditDateModel):
    name = models.CharField(max_length=100, blank=True)  # django admin (optional)
    image = models.ImageField(default="placeholder.png")
    description = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    num_reviews = models.IntegerField(default=0)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    current_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    count_in_stock = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, max_length=50, null=True)
    state = models.BooleanField(default=True)

    # ## Relations (User 1:N Products) - la FK se crea aqui
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, to_field="code"
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, to_field="code"
    )
    measurements = models.ManyToManyField(ProductMeasurement)

    class Meta:
        indexes = [models.Index(fields=["slug"])]  # create index for slug field


# ### Reviews =====================
class Reviews(AuditDateModel):
    description = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # createdAt x default

    # ## Relations
    # (Product 1:N Reviews)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
