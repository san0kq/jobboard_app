from django.contrib import admin

from .models import (
    Company,
    Contract,
    Employee,
    EmployeesNumber,
    Language,
    LanguageLevel,
    Level,
    Position,
    ProfileLanguage,
    Rating,
    Response,
    Review,
    ReviewRating,
    Salary,
    Sector,
    SocialLink,
    Status,
    Tag,
    Vacancy,
    WorkFormat,
)

admin.site.register(Rating)
admin.site.register(Position)
admin.site.register(EmployeesNumber)
admin.site.register(Sector)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(ReviewRating)
admin.site.register(SocialLink)
admin.site.register(Response)
admin.site.register(Contract)
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(Level)
admin.site.register(ProfileLanguage)
admin.site.register(Salary)
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(WorkFormat)
