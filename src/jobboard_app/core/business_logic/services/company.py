import uuid
from typing import Any

from accounts.models import Adress, City, Country
from core.business_logic.dto import (
    AddCompanyDTO,
    AddReviewDTO,
    AddSocialLinkDTO,
    CompanyFilterDTO,
)
from core.business_logic.exceptions import CompanyAlreadyExists, ReviewAlreadyExists
from core.models import Company, EmployeesNumber, Review, Sector, SocialLink
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Count


def get_company_all(company_filter: CompanyFilterDTO) -> list[Company]:
    companies = Company.objects.select_related("employees_number").prefetch_related("sectors")

    if company_filter.name:
        print(company_filter.name)
        companies = companies.filter(name__icontains=company_filter.name)
        print(companies)

    if company_filter.employees_number:
        for number in company_filter.employees_number:
            companies = companies.filter(employees_number__size_range=number)

    if company_filter.sectors:
        for sector in company_filter.sectors:
            companies = companies.filter(sectors__name=sector)

    companies = companies.annotate(vacancy__count=Count("vacancy__id")).order_by("-vacancy__count")
    return list(companies)


def add_company(company_data: AddCompanyDTO, sociallink_data: list[AddSocialLinkDTO]) -> None:
    with transaction.atomic():
        if Company.objects.filter(name__icontains=company_data.name).exists():
            raise CompanyAlreadyExists(f"Company {company_data.name} is already exists.")
        logo_extansion = company_data.logo.name.split(".")[-1]
        logo_name = str(uuid.uuid4()) + "." + logo_extansion
        company_data.logo.name = logo_name

        if not company_data.office_number:
            company_data.office_number = 0

        city = City.objects.get_or_create(
            name=company_data.city.capitalize(), country=Country.objects.get(name=company_data.country)
        )
        adress = Adress.objects.get_or_create(
            city=city[0],
            street=company_data.street,
            house_number=company_data.house_number,
            office_number=company_data.office_number,
        )

        sectors = [Sector.objects.get(name=sector) for sector in company_data.sectors]
        employyes_number = EmployeesNumber.objects.get(size_range=company_data.employees_number)

        company = Company.objects.create(
            name=company_data.name,
            employees_number=employyes_number,
            founded_in=company_data.founded_in,
            logo=company_data.logo,
            description=company_data.description,
            email=company_data.email,
            phone_number=company_data.phone_number,
            web_site=company_data.web_site,
            adress=adress[0],
        )
        company.sectors.set(sectors)

        if sociallink_data:
            for social_link in sociallink_data:
                SocialLink.objects.create(platform=social_link.platform, url=social_link.url, company=company)


def get_company_by_pk(pk: int) -> Any:
    company = (
        Company.objects.select_related("employees_number", "adress").prefetch_related("sectors").get(pk=pk)
    )
    return company


def add_review(review_data: AddReviewDTO, company_pk: int) -> None:
    user = User.objects.get(pk=1)
    company = Company.objects.get(pk=company_pk)

    if not Review.objects.filter(user=user, company=company).exists():
        Review.objects.create(text=review_data.text, user=user, company=company)
    else:
        raise ReviewAlreadyExists("The company already has a review from this user.")
