from django.db import models

from backend.models import AuditDateModel
from users.models import User
from .product_model import Product


# ### Reviews =====================
class Reviews(AuditDateModel):
    description = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # createdAt x default

    # ## Relations
    # (Product 1:N Reviews)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
