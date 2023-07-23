from dataclasses import dataclass

from django.core.files import File


@dataclass
class CompanyFilterDTO:
    name: str
    employees_number: list[str] | None
    sectors: list[str] | None


@dataclass
class AddCompanyDTO:
    name: str
    employees_number: str
    founded_in: int
    logo: File
    description: str
    email: str
    phone_number: str
    web_site: str
    country: str
    city: str
    street: str
    house_number: int
    office_number: int | None
    sectors: list[str]


@dataclass
class AddReviewDTO:
    text: str
