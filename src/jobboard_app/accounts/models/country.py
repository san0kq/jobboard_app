from django.db import models

from .base import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Country")

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return f"{self.name}"
