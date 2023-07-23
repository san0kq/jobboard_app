from django.db import models

from .base import BaseModel


class Sector(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Sector")

    class Meta:
        verbose_name_plural = "Sectors"

    def __str__(self) -> str:
        return f"{self.name}"
