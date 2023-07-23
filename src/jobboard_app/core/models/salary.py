from django.db import models

from .base import BaseModel


class Salary(BaseModel):
    min_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    max_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        unique_together = ("min_salary", "max_salary")
        verbose_name_plural = "Salaries"

    def __str__(self) -> str:
        return f"{self.min_salary} - {self.max_salary}"
