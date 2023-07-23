from django.db import models

from .base import BaseModel


class LanguageLevel(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="Language level")

    class Meta:
        verbose_name_plural = "Language levels"

    def __str__(self) -> str:
        return f"{self.name}"
