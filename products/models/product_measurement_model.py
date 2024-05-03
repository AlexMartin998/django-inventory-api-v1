from django.db import models

from backend.shared.models.models import AuditDateModel


class ProductMeasurement(AuditDateModel):
    name = models.CharField(max_length=150)
    nomenclature = models.CharField(max_length=21)
    code = models.CharField(max_length=150, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=["code"])]

