from accounts.models import Country
from core.models import Company, Contract, Level, WorkFormat
from core.presentation.validators import (
    TagsValidator,
    ValidateFileExtension,
    ValidateFileSize,
    phone_number_validator,
)
from django import forms

LEVELS = [(level.name, level.name) for level in Level.objects.all()]
COMPANIES = [(company.name, company.name) for company in Company.objects.all()]
COUNTRIES = [(country.name, country.name) for country in Country.objects.all()]
CONTRACTS = [(contract.name, contract.name) for contract in Contract.objects.all()]
WORK_FORMATS = [(work_format.name, work_format.name) for work_format in WorkFormat.objects.all()]


class VacancyFilterForm(forms.Form):
    name = forms.CharField(label="Position", max_length=100, strip=True, required=False)
    company = forms.CharField(label="Company", max_length=150, strip=True, required=False)
    levels = forms.MultipleChoiceField(label="Levels", choices=LEVELS, required=False)
    experience = forms.IntegerField(label="Experience", min_value=0, required=False)
    min_salary = forms.IntegerField(label="Min Salary", min_value=0, required=False)
    max_salary = forms.IntegerField(label="Max Salary", min_value=0, required=False)
    tag = forms.CharField(label="Tag", required=False)


class AddVacancyForm(forms.Form):
    name = forms.CharField(max_length=100, label="Vacancy name", strip=True)
    description = forms.CharField(max_length=500, label="Description", widget=forms.Textarea, strip=True)
    min_salary = forms.DecimalField(
        max_digits=10, decimal_places=2, min_value=0, max_value=1000000, required=False
    )
    max_salary = forms.DecimalField(
        max_digits=10, decimal_places=2, min_value=0, max_value=1000000, required=False
    )
    company = forms.ChoiceField(label="Company name", choices=COMPANIES)
    countries = forms.MultipleChoiceField(label="Countries", choices=COUNTRIES)
    contracts = forms.MultipleChoiceField(label="Contracts", choices=CONTRACTS)
    levels = forms.MultipleChoiceField(label="Levels", choices=LEVELS)
    work_formats = forms.MultipleChoiceField(label="Work formats", choices=WORK_FORMATS)
    tags = forms.CharField(
        max_length=250, widget=forms.Textarea, required=False, validators=[TagsValidator(max_number=6)]
    )
    years_exp = forms.IntegerField(max_value=120, required=False)


class AddResponseForm(forms.Form):
    text = forms.CharField(label="Text", max_length=500, widget=forms.Textarea, strip=True)
    resume = forms.FileField(
        label="Resume",
        allow_empty_file=False,
        required=False,
        validators=[ValidateFileExtension(["pdf"]), ValidateFileSize(max_size=5_000_000)],
    )
    phone_number = forms.CharField(
        label="Phone number", max_length=20, validators=[phone_number_validator], strip=True
    )
