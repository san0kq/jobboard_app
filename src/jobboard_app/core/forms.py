from django import forms

from .models import Adress, Company, Response, Review, Vacancy


class VacancyModelForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ["adress"]


class AdressModelForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"


class ResponseModelForm(forms.ModelForm):
    class Meta:
        model = Response
        exclude = ["user", "vacancy", "status"]


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["user", "company"]
