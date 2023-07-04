from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .forms import (
    AdressModelForm,
    CompanyModelForm,
    ResponseModelForm,
    ReviewModelForm,
    VacancyModelForm,
)
from .models import Company, Vacancy


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        vacancies = Vacancy.objects.all()
        context = {"vacancies": vacancies}
        return render(request, "index.html", context=context)


class AddVacancyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = VacancyModelForm()
        return render(request, "add_vacancy.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = VacancyModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("index")


class CompaniesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        companies = Company.objects.all()
        context = {"companies": companies}
        return render(request, "companies.html", context=context)


class AddCompanyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        company_form = CompanyModelForm()
        adress_form = AdressModelForm()
        context = {"company_form": company_form, "adress_form": adress_form}
        return render(request, "add_company.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        company_form = CompanyModelForm(request.POST)
        adress_form = AdressModelForm(request.POST)
        if adress_form.is_valid() and company_form.is_valid():
            adress = adress_form.save()
            company = company_form.save(commit=False)
            company.adress = adress
            company.save()

        return redirect("company-list")


class VacancyView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        vacancy = Vacancy.objects.get(pk=pk)
        context = {"vacancy": vacancy}
        return render(request, "vacancy.html", context=context)


class VacancyApplyView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = ResponseModelForm()
        vacancy = Vacancy.objects.get(pk=pk)
        context = {"form": form, "vacancy": vacancy}
        return render(request, "add_response.html", context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = ResponseModelForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.vacancy = Vacancy.objects.get(pk=pk)
            response.user = User.objects.get(pk=1)
            response.save()

        return redirect("index")


class CompanyView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        company = Company.objects.get(pk=pk)
        context = {"company": company}
        return render(request, "company.html", context=context)


class CompanyAddReviewView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        company = Company.objects.get(pk=pk)
        form = ReviewModelForm()
        context = {"company": company, "form": form}
        return render(request, "add_review.html", context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company = Company.objects.get(pk=pk)
            review.user = User.objects.get(pk=1)
            review.save()

        return redirect("company", pk=pk)
