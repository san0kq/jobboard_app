from typing import Any

from core.models import (
    Contract,
    EmployeesNumber,
    Language,
    LanguageLevel,
    Level,
    Rating,
    Sector,
    Status,
    WorkFormat,
)
from django.db import migrations

DEFAULT_LEVELS = ("Intern", "Junior", "Middle", "Senior")
DEFAULT_CONTRACTS = ("Employment contract", "B2B", "Mandate contract")
DEFAULT_LANGUAGE_LEVELS = (
    "Elementary",
    "Pre-Intermidiate",
    "Intermediate",
    "Upper-Intermidiate",
    "Advanced",
    "Native",
)
DEFAULT_LANGUAGES = (
    "English",
    "Russian",
    "Belarusian",
    "Ukrain",
    "Polish",
    "Chinese",
    "Hindi",
    "Spanish",
    "French",
    "Arabic",
    "Bengali",
    "Portuguese",
    "Urdu",
    "Indonesian",
    "German",
    "Japanese",
    "Nigerian Pidgin",
    "Marathi",
    "Telugu",
    "Turkish",
    "Tamil",
    "Vietnamese",
)
DEFAULT_RATINGS = ("Like", "Dislike")
DEFAULT_STATUSES = (
    "Open to work",
    "Open for proposals",
    "Not open for proposals",
    "Created",
    "Viewed",
    "Rejected",
    "Accepted for work",
)
DEFAULT_WORK_FORMATS = ("Remote", "Office", "Hybrid", "Full-time", "Part-time", "Freelance")
DEFAULT_EMPLOYEES_NUMBER = ("Up to 50", "51-100", "101-500", "510-1000", "From 1000")
DEFAULT_SECTORS = ("Web", "Mobile", "AI", "Telecommunications")


def populate_levels_table(apps: Any, schema_editor: Any) -> None:
    for level in DEFAULT_LEVELS:
        Level.objects.create(name=level)


def reverse_levels_table(apps: Any, schema_editor: Any) -> None:
    for level in DEFAULT_LEVELS:
        Level.objects.get(name=level).delete()


def populate_contracts_table(apps: Any, schema_editor: Any) -> None:
    for contract in DEFAULT_CONTRACTS:
        Contract.objects.create(name=contract)


def reverse_contracts_table(apps: Any, schema_editor: Any) -> None:
    for contract in DEFAULT_CONTRACTS:
        Contract.objects.get(name=contract).delete()


def populate_language_levels_table(apps: Any, schema_editor: Any) -> None:
    for language_level in DEFAULT_LANGUAGE_LEVELS:
        LanguageLevel.objects.create(name=language_level)


def reverse_language_levels_table(apps: Any, schema_editor: Any) -> None:
    for language_level in DEFAULT_LANGUAGE_LEVELS:
        LanguageLevel.objects.get(name=language_level).delete()


def populate_languages_table(apps: Any, schema_editor: Any) -> None:
    for language in DEFAULT_LANGUAGES:
        Language.objects.create(name=language)


def reverse_languages_table(apps: Any, schema_editor: Any) -> None:
    for language in DEFAULT_LANGUAGES:
        Language.objects.get(name=language).delete()


def populate_ratings_table(apps: Any, schema_editor: Any) -> None:
    for rating in DEFAULT_RATINGS:
        Rating.objects.create(name=rating)


def reverse_ratings_table(apps: Any, schema_editor: Any) -> None:
    for rating in DEFAULT_RATINGS:
        Rating.objects.get(name=rating).delete()


def populate_statuses_table(apps: Any, schema_editor: Any) -> None:
    for status in DEFAULT_STATUSES:
        Status.objects.create(name=status)


def reverse_statuses_table(apps: Any, schema_editor: Any) -> None:
    for status in DEFAULT_STATUSES:
        Status.objects.get(name=status).delete()


def populate_work_formats_table(apps: Any, schema_editor: Any) -> None:
    for work_format in DEFAULT_WORK_FORMATS:
        WorkFormat.objects.create(name=work_format)


def reverse_work_formats_table(apps: Any, schema_editor: Any) -> None:
    for work_format in DEFAULT_WORK_FORMATS:
        WorkFormat.objects.get(name=work_format).delete()


def populate_employees_number_table(apps: Any, schema_editor: Any) -> None:
    for number in DEFAULT_EMPLOYEES_NUMBER:
        EmployeesNumber.objects.create(size_range=number)


def reverse_employees_number_table(apps: Any, schema_editor: Any) -> None:
    for number in DEFAULT_EMPLOYEES_NUMBER:
        EmployeesNumber.objects.get(size_range=number).delete()


def populate_sectors_table(apps: Any, schema_editor: Any) -> None:
    for sector in DEFAULT_SECTORS:
        Sector.objects.create(name=sector)


def reverse_sectors_table(apps: Any, schema_editor: Any) -> None:
    for sector in DEFAULT_SECTORS:
        Sector.objects.get(name=sector).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            code=populate_levels_table,
            reverse_code=reverse_levels_table,
        ),
        migrations.RunPython(
            code=populate_contracts_table,
            reverse_code=reverse_contracts_table,
        ),
        migrations.RunPython(
            code=populate_language_levels_table,
            reverse_code=reverse_language_levels_table,
        ),
        migrations.RunPython(
            code=populate_languages_table,
            reverse_code=reverse_languages_table,
        ),
        migrations.RunPython(
            code=populate_ratings_table,
            reverse_code=reverse_ratings_table,
        ),
        migrations.RunPython(
            code=populate_statuses_table,
            reverse_code=reverse_statuses_table,
        ),
        migrations.RunPython(
            code=populate_work_formats_table,
            reverse_code=reverse_work_formats_table,
        ),
        migrations.RunPython(
            code=populate_employees_number_table,
            reverse_code=reverse_employees_number_table,
        ),
        migrations.RunPython(
            code=populate_sectors_table,
            reverse_code=reverse_sectors_table,
        ),
    ]
