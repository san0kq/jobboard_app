from django.db import models

from .base import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name="Company name")
    employees_number = models.ForeignKey(
        to="EmployeesNumber",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="companies",
        related_query_name="company",
    )
    founded_in = models.PositiveSmallIntegerField()
    logo = models.ImageField(upload_to="image/logo/", null=True, blank=True)
    description = models.TextField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    web_site = models.URLField(max_length=200)
    adress = models.OneToOneField(
        to="accounts.Adress", on_delete=models.SET_NULL, null=True, blank=True, related_name="company"
    )
    sectors = models.ManyToManyField(to="Sector", related_name="companies", related_query_name="company")

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return f"{self.name}"
