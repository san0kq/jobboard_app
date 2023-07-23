from django.db import models

from .base import BaseModel


class Adress(BaseModel):
    city = models.ForeignKey(
        to="City", on_delete=models.CASCADE, related_name="adresses", related_query_name="adress"
    )
    street = models.CharField(max_length=30)
    house_number = models.PositiveSmallIntegerField()
    office_number = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Adresses"
        unique_together = ("city", "street", "house_number", "office_number")

    def __str__(self) -> str:
        if self.office_number:
            return f"{self.city}-{self.street}-{self.house_number}-{self.office_number}"
        else:
            return f"{self.city}-{self.street}-{self.house_number}"
