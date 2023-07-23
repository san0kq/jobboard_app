from django.db import models

from .base import BaseModel


class Status(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="Status")

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self) -> str:
        return f"{self.name}"
