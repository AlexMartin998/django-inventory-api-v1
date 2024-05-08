from django.db import models

from backend.shared.models.models import AuditDateModel


class Aaran(AuditDateModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
