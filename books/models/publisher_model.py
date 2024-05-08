from django.db import models

from backend.shared.models.models import AuditDateModel


class Publisher(AuditDateModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        indexes = [models.Index(fields=["name", "code"])]
        ordering = ["name"]
