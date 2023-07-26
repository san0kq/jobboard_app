from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from core.business_logic.dto import (
    AddCompanyDTO,
    AddReviewDTO,
    AddSocialLinkDTO,
    CompanyFilterDTO,
)
from core.business_logic.exceptions import CompanyAlreadyExists, ReviewAlreadyExists
from core.business_logic.services import (
    add_company,
    add_review,
    get_company_all,
    get_company_by_pk,
)
from core.presentation.converters import convert_data_from_form_to_dto
from core.presentation.forms import (
    AddCompanyForm,
    AddReviewForm,
    AddSocialLinkForm,
    CompanyFilterForm,
)


class CompaniesView(View):
    def get(self, request: HttpRequest) -> Optional[HttpResponse]:
        filters_form = CompanyFilterForm(request.GET)
        if filters_form.is_valid():
            filter_data = convert_data_from_form_to_dto(
                dto=CompanyFilterDTO, data_from_form=filters_form.cleaned_data
            )
            companies = get_company_all(company_filter=filter_data)
            form = CompanyFilterForm()
            context = {"companies": companies, "form": form}
            return render(request, "companies.html", context=context)
        else:
            return None


class AddCompanyView(View):
    SocialLinkFormSet = formset_factory(AddSocialLinkForm, extra=1)

    def get(self, request: HttpRequest) -> HttpResponse:
        company_form = AddCompanyForm()
        sociallink_formset = self.SocialLinkFormSet()
        context = {"company_form": company_form, "sociallink_formset": sociallink_formset}
        return render(request, "add_company.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
        company_form = AddCompanyForm(request.POST, files=request.FILES)
        sociallink_formset = self.SocialLinkFormSet(request.POST)

        if company_form.is_valid() and sociallink_formset.is_valid():
            company_form_data = convert_data_from_form_to_dto(
                dto=AddCompanyDTO, data_from_form=company_form.cleaned_data
            )
            sociallink_form_data_list = []
            for form in sociallink_formset:
                if form.cleaned_data:
                    sociallink_form_data = convert_data_from_form_to_dto(
                        dto=AddSocialLinkDTO, data_from_form=form.cleaned_data
                    )
                    sociallink_form_data_list.append(sociallink_form_data)
            try:
                add_company(company_data=company_form_data, sociallink_data=sociallink_form_data_list)
            except CompanyAlreadyExists as err:
                error_message = err
                context = {
                    "company_form": company_form,
                    "sociallink_formset": sociallink_formset,
                    "error_message": error_message,
                }
                return render(request, "add_company.html", context=context)

        else:
            context = {"company_form": company_form, "sociallink_formset": sociallink_formset}
            return render(request, "add_company.html", context=context)

        return redirect("company-list")


class CompanyView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        company = get_company_by_pk(pk=pk)
        context = {"company": company}
        return render(request, "company.html", context=context)


class AddReviewView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = AddReviewForm()
        company = get_company_by_pk(pk=pk)
        context = {"company": company, "form": form}
        return render(request, "add_review.html", context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect | HttpResponse:
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review_data = convert_data_from_form_to_dto(dto=AddReviewDTO, data_from_form=form.cleaned_data)
            try:
                add_review(review_data=review_data, company_pk=pk)
            except ReviewAlreadyExists:
                company = get_company_by_pk(pk=pk)
                error_message = (
                    "You have already left a review for this company. "
                    "You can delete it and write a new one."
                )
                context = {"company": company, "form": form, "error_message": error_message}
                return render(request, "add_review.html", context=context)

        else:
            company = get_company_by_pk(pk=pk)
            return render(request, "add_review.html", {"company": company, "form": form})

        return redirect("company", pk=pk)
