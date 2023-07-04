from django.urls import path

from .views import (
    AddCompanyView,
    AddVacancyView,
    CompaniesView,
    CompanyAddReviewView,
    CompanyView,
    IndexView,
    VacancyApplyView,
    VacancyView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("vacancy/add/", AddVacancyView.as_view(), name="add-vacancy"),
    path("companies/", CompaniesView.as_view(), name="company-list"),
    path("company/add/", AddCompanyView.as_view(), name="add-company"),
    path("vacancy/<int:pk>", VacancyView.as_view(), name="vacancy"),
    path("vacancy/<int:pk>/apply", VacancyApplyView.as_view(), name="vacancy-apply"),
    path("company/<int:pk>", CompanyView.as_view(), name="company"),
    path("company/<int:pk>/review", CompanyAddReviewView.as_view(), name="company-review"),
]
