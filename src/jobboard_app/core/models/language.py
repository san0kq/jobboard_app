from django.db import models

from .base import BaseModel


class Language(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="Language")

    class Meta:
        verbose_name_plural = "Languages"

    def __str__(self) -> str:
        return f"{self.name}"
