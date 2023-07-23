from django.db import models

from .base import BaseModel


class Contract(BaseModel):
    name = models.CharField(max_length=40, unique=True, verbose_name="Contract")

    class Meta:
        verbose_name_plural = "Contracts"

    def __str__(self) -> str:
        return f"{self.name}"
