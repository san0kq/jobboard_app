from django.core.validators import MaxValueValidator
from django.db import models

from .base import BaseModel


class Vacancy(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Vacancy name")
    employee = models.ForeignKey(
        to="Employee", on_delete=models.CASCADE, related_name="vacancies", related_query_name="vacancy"
    )
    description = models.TextField(max_length=500)
    salary = models.ForeignKey(
        to="Salary",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vacancies",
        related_query_name="vacancy",
    )
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, related_name="vacancies", related_query_name="vacancy"
    )
    countries = models.ManyToManyField(
        to="accounts.Country", related_name="vacancies", related_query_name="vacancy"
    )
    contracts = models.ManyToManyField(to="Contract", related_name="vacancies", related_query_name="vacancy")
    levels = models.ManyToManyField(to="Level", related_name="vacancies", related_query_name="vacancy")
    work_formats = models.ManyToManyField(
        to="WorkFormat", related_name="vacancies", related_query_name="vacancy"
    )
    tags = models.ManyToManyField(to="Tag", related_name="vacancies", related_query_name="vacancy")
    years_exp = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], default=0, verbose_name="Years experience"
    )

    class Meta:
        verbose_name_plural = "Vacancies"

    def __str__(self) -> str:
        return f"{self.name} in {self.company.name}"
