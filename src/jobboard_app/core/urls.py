from django.urls import path

from .views import AddVacancyView, CompaniesView, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('add/', AddVacancyView.as_view(), name='add_vacancy'),
    path('companies/', CompaniesView.as_view(), name='companies'),
]
