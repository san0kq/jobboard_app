from django.contrib import admin

from .models import (
    Adress,
    Company,
    Employee,
    EmployeesNumber,
    Position,
    Rating,
    Response,
    Review,
    ReviewRating,
    Sector,
    SocialLink,
    Vacancy,
)

admin.site.register(Rating)
admin.site.register(Position)
admin.site.register(Adress)
admin.site.register(EmployeesNumber)
admin.site.register(Sector)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(ReviewRating)
admin.site.register(SocialLink)
admin.site.register(Response)
