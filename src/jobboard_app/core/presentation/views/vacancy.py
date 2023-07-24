from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

from core.business_logic.dto import AddResponseDTO, AddVacancyDTO, VacancyFilterDTO
from core.business_logic.services import (
    add_response,
    add_vacancy,
    get_vacancy_all,
    get_vacancy_by_pk,
)
from core.presentation.converters import convert_data_from_form_to_dto
from core.presentation.forms import AddResponseForm, AddVacancyForm, VacancyFilterForm


class IndexView(View):
    def get(self, request: HttpRequest) -> Optional[HttpResponse]:
        filters_form = VacancyFilterForm(request.GET)
        if filters_form.is_valid():
            filter_data = convert_data_from_form_to_dto(
                dto=VacancyFilterDTO, data_from_form=filters_form.cleaned_data
            )
            vacancies = get_vacancy_all(vacancy_filter=filter_data)
            form = VacancyFilterForm()
            context = {"vacancies": vacancies, "form": form}
            return render(request, "index.html", context=context)
        else:
            return None


class AddVacancyView(View):
    def get(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
        form = AddVacancyForm()
        return render(request, "add_vacancy.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = AddVacancyForm(request.POST)
        if form.is_valid():
            form_data = convert_data_from_form_to_dto(dto=AddVacancyDTO, data_from_form=form.cleaned_data)
            add_vacancy(vacancy_data=form_data)
        else:
            return render(request, "add_vacancy.html", {"form": form})

        return redirect("index")


class VacancyView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        vacancy = get_vacancy_by_pk(pk=pk)
        context = {"vacancy": vacancy}
        return render(request, "vacancy.html", context=context)


class AddResponseView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = AddResponseForm()
        vacancy = get_vacancy_by_pk(pk=pk)
        context = {"form": form, "vacancy": vacancy}
        return render(request, "add_response.html", context=context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect | HttpResponse:
        form = AddResponseForm(request.POST, files=request.FILES)
        if form.is_valid():
            response_data = convert_data_from_form_to_dto(dto=AddResponseDTO, data_from_form=form.cleaned_data)
            add_response(response_data=response_data, vacancy_pk=pk)
        else:
            vacancy = get_vacancy_by_pk(pk=pk)
            return render(request, "add_response.html", {"form": form, "vacancy": vacancy})
        return redirect("index")
