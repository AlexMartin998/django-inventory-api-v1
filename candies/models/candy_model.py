from django.db import models

from backend.shared.models.models import AuditDateModel


class Candy(AuditDateModel):
    name = models.CharField(max_length=100)
