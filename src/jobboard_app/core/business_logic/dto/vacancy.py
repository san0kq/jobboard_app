from dataclasses import dataclass
from typing import Any

from django.core.files import File


@dataclass
class VacancyFilterDTO:
    name: str
    company: str
    levels: list[str] | None
    experience: int | None
    min_salary: int | None
    max_salary: int | None
    tag: str


@dataclass
class AddVacancyDTO:
    name: str
    description: str
    min_salary: Any  # Decimal
    max_salary: Any  # Decimal
    company: str
    countries: list[str]
    contracts: list[str]
    levels: list[str]
    work_formats: list[str]
    tags: str | None
    years_exp: int | None


@dataclass
class AddResponseDTO:
    text: str
    resume: File | None
    phone_number: str
