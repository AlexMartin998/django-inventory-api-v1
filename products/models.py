from django.db import models

from backend.models import AuditDateModel
from users.models import User



# como AuditDateModel ya hereda de models.Model, no es necesario hacerlo en Product
class Category(AuditDateModel):
    name = models.CharField(max_length=210, blank=True)
    description = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=210, blank=True, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['code']) # create index for code field
        ]

class SubCategory(AuditDateModel):
    name = models.CharField(max_length=210, blank=True)
    description = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=210, blank=True, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['code'])
        ]

class ProductMeasurement(AuditDateModel):
    name = models.CharField(max_length=150, blank=True)
    nomenclature = models.CharField(max_length=21, blank=True)
    code = models.CharField(max_length=150, blank=True, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['code'])
        ]




class Product(AuditDateModel):
    name = models.CharField(
        max_length=100,
        blank=True  # django admin (optional)
    )
    image = models.ImageField(default='placeholder.png')
    description = models.CharField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(default=0)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    current_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    count_in_stock = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, max_length=50, null=True, blank=True)
    state = models.BooleanField(default=True)

    # ## Relations (User 1:N Products) - la FK se crea aqui
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, to_field='code')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, to_field='code')
    measurements = models.ManyToManyField(ProductMeasurement, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['slug']) # create index for slug field
        ]





# ### Reviews =====================

class Reviews(AuditDateModel):
    description = models.CharField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # createdAt x default

    # ## Relations
    # (Product 1:N Reviews)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

