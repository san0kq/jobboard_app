from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.business_logic.dto import (
        AddCompanyDTO,
        AddReviewDTO,
        AddSocialLinkDTO,
        CompanyFilterDTO,
    )

from accounts.models import Address, City, Country
from core.business_logic.exceptions import CompanyAlreadyExists, ReviewAlreadyExists
from core.business_logic.services.common import change_file_size, rename_file_to_uuid
from core.models import Company, EmployeesNumber, Review, Sector, SocialLink
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Count

logger = getLogger(__name__)


def get_company_all(company_filter: CompanyFilterDTO) -> list[Company]:
    companies = Company.objects.select_related("employees_number").prefetch_related("sectors")

    if company_filter.name:
        companies = companies.filter(name__icontains=company_filter.name)

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
            logger.error("Company is already exists.", extra={"company_name": company_data.name})
            raise CompanyAlreadyExists(f"Company {company_data.name} is already exists.")
        company_data.logo = rename_file_to_uuid(file=company_data.logo)
        company_data.logo = change_file_size(file=company_data.logo)
        logger.info("Company logo uploaded", extra={"logo_path": company_data.logo.name})
        if not company_data.office_number:
            company_data.office_number = 0

        city = City.objects.get_or_create(
            name=company_data.city.capitalize(), country=Country.objects.get(name=company_data.country)
        )
        address = Address.objects.get_or_create(
            city=city[0],
            street=company_data.street,
            house_number=company_data.house_number,
            office_number=company_data.office_number,
        )[0]

        if Company.objects.filter(address=address.pk).exists():
            logger.error("The company with such address already exist", extra={"address_id": address.pk})
            raise CompanyAlreadyExists("The company with such address already exist")

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
            address=address,
        )
        company.sectors.set(sectors)

        if sociallink_data:
            for social_link in sociallink_data:
                SocialLink.objects.create(platform=social_link.platform, url=social_link.url, company=company)
                logger.info(
                    "New company social_link created",
                    extra={"company_name": company_data.name, "url": social_link.url},
                )
        logger.info("New company created.", extra={"company_name": company_data.name})


def get_company_by_pk(pk: int) -> Company:
    company: Company = (
        Company.objects.select_related("employees_number", "address").prefetch_related("sectors").get(pk=pk)
    )
    logger.info("Successfully got company.", extra={"company_id": pk})
    return company


def add_review(review_data: AddReviewDTO, company_pk: int) -> None:
    user_model = get_user_model()
    user = user_model.objects.get(pk=1)
    company = Company.objects.get(pk=company_pk)

    if not Review.objects.filter(user=user, company=company).exists():
        review = Review.objects.create(text=review_data.text, user=user, company=company)
        logger.info(
            "New review created.", extra={"company_id": company_pk, "user_id": user.pk, "review_id": review.pk}
        )
    else:
        logger.error(
            "The company already has a review from this user.",
            extra={"company_id": company_pk, "user_id": user.pk},
        )
        raise ReviewAlreadyExists("The company already has a review from this user.")
