from django.db import models

from .base import BaseModel


class EmployeesNumber(BaseModel):
    size_range = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Employees numbers"

    def __str__(self) -> str:
        return f"{self.size_range}"
