from django.db import models

from .base import BaseModel


class Rating(BaseModel):
    name = models.CharField(max_length=20, unique=True, verbose_name="Rating")

    class Meta:
        verbose_name_plural = "Ratings"

    def __str__(self) -> str:
        return f"{self.name}"
