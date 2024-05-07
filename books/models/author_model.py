from django.db import models

from backend.shared.models.models import AuditDateModel


class Author(AuditDateModel):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    code = models.CharField(max_length=10, unique=True)
    state = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["code"], name="idx_author_code"),
        ]
