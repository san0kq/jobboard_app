from django.db import models

from .base import BaseModel


class Level(BaseModel):
    name = models.CharField(max_length=40, unique=True, verbose_name="Level")

    class Meta:
        verbose_name_plural = "Levels"

    def __str__(self) -> str:
        return f"{self.name}"
