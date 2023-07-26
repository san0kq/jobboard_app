from django.contrib import admin

from .models import Address, City, Country, Gender, Profile

admin.site.register(Gender)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Address)
