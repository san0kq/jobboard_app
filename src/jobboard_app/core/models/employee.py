from django.db import models

from .base import BaseModel


class Employee(BaseModel):
    user = models.OneToOneField(
        to="auth.User", primary_key=True, on_delete=models.CASCADE, related_name="employee"
    )
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, related_name="employees", related_query_name="employee"
    )
    phone_number = models.CharField(max_length=20)
    city = models.ForeignKey(
        to="accounts.City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
        related_query_name="employee",
    )
    image = models.ImageField(upload_to="image/avatar/", null=True, blank=True)
    positions = models.ManyToManyField(to="Position", related_name="employees", related_query_name="employee")

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.company.name}"
