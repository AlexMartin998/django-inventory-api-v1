from django.db import models

from backend.shared.models.models import AuditDateModel


class Aba(AuditDateModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["code"], name="aba_code_idx"),
        ]
