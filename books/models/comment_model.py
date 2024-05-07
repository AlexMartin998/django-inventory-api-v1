from django.db import models

from backend.shared.models.models import AuditDateModel


class Comment(AuditDateModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=["name", "email"])]
