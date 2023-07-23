from datetime import date

from accounts.models import Country
from core.models import EmployeesNumber, Sector
from core.presentation.validators import (
    ValidateFileExtension,
    ValidateFileSize,
    phone_number_validator,
)
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

EMPLOYEES_NUMBERS = [(number.size_range, number.size_range) for number in EmployeesNumber.objects.all()]
COUNTRIES = [(country.name, country.name) for country in Country.objects.all()]
SECTORS = [(sector.name, sector.name) for sector in Sector.objects.all()]


class AddCompanyForm(forms.Form):
    name = forms.CharField(max_length=150, label="Company name", strip=True)
    employees_number = forms.ChoiceField(label="Employees number", choices=EMPLOYEES_NUMBERS)
    founded_in = forms.IntegerField(
        label="Founded in (year)", validators=[MaxValueValidator(date.today().year), MinValueValidator(1500)]
    )
    logo = forms.ImageField(
        label="Logo",
        allow_empty_file=False,
        validators=[ValidateFileExtension(["jpg", "png"]), ValidateFileSize(5_000_000)],
    )
    description = forms.CharField(max_length=500, label="Description", widget=forms.Textarea, strip=True)
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(
        label="Phone number", validators=[phone_number_validator], max_length=20, min_length=5
    )
    web_site = forms.URLField(
        label="Web site",
        max_length=200,
        error_messages={"invalid": "Invalid URL. Example: https://www.job-board.by"},
    )
    country = forms.ChoiceField(label="Country", choices=COUNTRIES)
    city = forms.CharField(label="City", max_length=50, strip=True)
    street = forms.CharField(label="Street", max_length=30, strip=True)
    house_number = forms.IntegerField(label="House number", validators=[MinValueValidator(1)])
    office_number = forms.IntegerField(
        label="Office number", validators=[MinValueValidator(1), MaxValueValidator(10000)], required=False
    )
    sectors = forms.MultipleChoiceField(label="Sectors", choices=SECTORS)


class AddReviewForm(forms.Form):
    text = forms.CharField(label="Text", max_length=800, widget=forms.Textarea, strip=True)


class CompanyFilterForm(forms.Form):
    name = forms.CharField(label="Company", max_length=150, strip=True, required=False)
    employees_number = forms.MultipleChoiceField(
        label="Employees number", choices=EMPLOYEES_NUMBERS, required=False
    )
    sectors = forms.MultipleChoiceField(label="Sectors", choices=SECTORS, required=False)
