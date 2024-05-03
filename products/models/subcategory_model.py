from django.db import models

from backend.shared.models.models import AuditDateModel


class SubCategory(AuditDateModel):
    name = models.CharField(max_length=210)
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=210, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=["code"])]

