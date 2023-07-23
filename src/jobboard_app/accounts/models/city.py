from django.db import models

from .base import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=50, verbose_name="City")
    country = models.ForeignKey(
        to="Country", on_delete=models.CASCADE, related_name="cities", related_query_name="city"
    )

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.name} - {self.country.name}"
