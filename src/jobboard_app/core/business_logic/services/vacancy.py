from __future__ import annotations

import uuid
from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.business_logic.dto import AddResponseDTO, AddVacancyDTO, VacancyFilterDTO

from accounts.models import Country
from core.business_logic.exceptions import ResponseAlreadyExists
from core.models import (
    Company,
    Contract,
    Employee,
    Level,
    Response,
    Salary,
    Tag,
    Vacancy,
    WorkFormat,
)
from django.contrib.auth import get_user_model
from django.db import transaction

logger = getLogger(__name__)


def get_vacancy_all(vacancy_filter: VacancyFilterDTO) -> list[Vacancy]:
    vacancies = Vacancy.objects.select_related("company", "salary").prefetch_related("levels", "tags")

    if vacancy_filter.name:
        vacancies = vacancies.filter(name__icontains=vacancy_filter.name)

    if vacancy_filter.company:
        vacancies = vacancies.filter(company__name__icontains=vacancy_filter.company)

    if vacancy_filter.levels:
        for level in vacancy_filter.levels:
            vacancies = vacancies.filter(levels__name=level)

    if vacancy_filter.experience:
        vacancies = vacancies.filter(years_exp=vacancy_filter.experience)

    if vacancy_filter.min_salary:
        vacancies = vacancies.filter(salary__min_salary__gte=vacancy_filter.min_salary)

    if vacancy_filter.max_salary:
        vacancies = vacancies.filter(salary__max_salary__lte=vacancy_filter.max_salary)

    if vacancy_filter.tag:
        vacancies = vacancies.filter(tags__name=vacancy_filter.tag)

    return list(vacancies)


def add_vacancy(vacancy_data: AddVacancyDTO) -> None:
    with transaction.atomic():
        if not vacancy_data.min_salary:
            vacancy_data.min_salary = 0
        if not vacancy_data.max_salary:
            vacancy_data.max_salary = 0

        salary = Salary.objects.get_or_create(
            min_salary=vacancy_data.min_salary, max_salary=vacancy_data.max_salary
        )[0]

        employee = Employee.objects.get(pk=1)
        company = Company.objects.get(name=vacancy_data.company)
        countries = [Country.objects.get(name=country) for country in vacancy_data.countries]
        contracts = [Contract.objects.get(name=contract) for contract in vacancy_data.contracts]
        levels = [Level.objects.get(name=level) for level in vacancy_data.levels]
        work_formats = [WorkFormat.objects.get(name=work_format) for work_format in vacancy_data.work_formats]

        vacancy = Vacancy.objects.create(
            name=vacancy_data.name,
            employee=employee,
            description=vacancy_data.description,
            salary=salary,
            company=company,
            years_exp=vacancy_data.years_exp,
        )
        vacancy.countries.set(countries)
        vacancy.contracts.set(contracts)
        vacancy.levels.set(levels)
        vacancy.work_formats.set(work_formats)

        if vacancy_data.tags:
            tags_list = vacancy_data.tags.split("\r\n")
            tags = [Tag.objects.get_or_create(name=tag)[0] for tag in tags_list]
            vacancy.tags.set(tags)

        logger.info("New vacancy created.", extra={"vacancy_id": vacancy.pk, "employee_id": employee.pk})


def get_vacancy_by_pk(pk: int) -> Vacancy:
    vacancy: Vacancy = (
        Vacancy.objects.select_related("employee", "salary", "company")
        .prefetch_related("countries", "contracts", "levels", "work_formats", "tags")
        .get(pk=pk)
    )
    logger.info("Successfully got vacancy.", extra={"vacancy_id": pk})
    return vacancy


def add_response(response_data: AddResponseDTO, vacancy_pk: int) -> None:
    user_model = get_user_model()
    user = user_model.objects.get(pk=1)
    vacancy = Vacancy.objects.get(pk=vacancy_pk)

    if not Response.objects.filter(user=user.pk, vacancy=vacancy.pk).exists():
        if response_data.resume:
            resume_extension = response_data.resume.name.split(".")[-1]
            resume_name = str(uuid.uuid4()) + "." + resume_extension
            response_data.resume.name = resume_name

        response = Response.objects.create(
            user=user,
            vacancy=vacancy,
            text=response_data.text,
            resume=response_data.resume,
            phone_number=response_data.phone_number,
        )

        if response_data.resume:
            logger.info("Response resume uploaded.", extra={"path": response_data.resume.name})
        logger.info(
            "New response created.",
            extra={"response_id": response.pk, "user_id": user.pk, "vacancy_id": vacancy_pk},
        )
    else:
        logger.error(
            "In response to this vacancy, there is already a response from this user.",
            extra={"vacancy_id": vacancy_pk, "user_id": user.pk},
        )
        raise ResponseAlreadyExists(
            "In response to this vacancy, there is already" " a response from this user."
        )
