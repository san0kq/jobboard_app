from django.db import models

from .base import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="Tag")

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return f"{self.name}"
