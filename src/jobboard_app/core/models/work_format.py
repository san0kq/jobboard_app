from django.db import models

from .base import BaseModel


class WorkFormat(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Work format")

    class Meta:
        verbose_name_plural = "Work formats"

    def __str__(self) -> str:
        return f"{self.name}"
