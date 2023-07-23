from django.db import models

from .base import BaseModel


class Gender(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="Gender")

    class Meta:
        verbose_name_plural = "Genders"

    def __str__(self) -> str:
        return f"{self.name}"
