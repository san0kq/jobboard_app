from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import redirect, render
from django.views import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .forms import VacancyForm
from .models import Company, Vacancy


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        vacancies = Vacancy.objects.all()
        data = {'vacancies': vacancies}
        return render(request, 'index.html', context=data)


class AddVacancyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = VacancyForm()
        return render(request, 'add_vacancy.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('index')


class CompaniesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        companies = Company.objects.all()
        data = {'companies': companies}
        return render(request, 'companies.html', context=data)
