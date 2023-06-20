from django.contrib import admin

from .models import (
    City,
    Contract,
    Country,
    Gender,
    Language,
    LanguageLevel,
    Level,
    Profile,
    ProfileLanguage,
    Salary,
    Status,
    Tag,
    WorkFormat,
)

admin.site.register(Gender)
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(WorkFormat)
admin.site.register(Status)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Contract)
admin.site.register(Level)
admin.site.register(Salary)
admin.site.register(ProfileLanguage)
admin.site.register(Profile)
admin.site.register(Tag)
