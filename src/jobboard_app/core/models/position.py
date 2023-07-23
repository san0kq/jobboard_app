from django.db import models

from .base import BaseModel


class Position(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Position")

    class Meta:
        verbose_name_plural = "Positions"

    def __str__(self) -> str:
        return f"{self.name}"
