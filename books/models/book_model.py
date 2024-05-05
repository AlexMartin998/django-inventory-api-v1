from django.db import models

from backend.shared.models.models import AuditDateModel


class Book(AuditDateModel):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=["code"])]  # create index for code field
