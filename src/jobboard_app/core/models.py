from accounts.models import (
    City,
    Contract,
    Country,
    Level,
    Profile,
    Salary,
    Status,
    Tag,
    WorkFormat,
)
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Rating(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Rating')

    class Meta:
        verbose_name_plural = 'Ratings'

    def __str__(self) -> str:
        return f'{self.name}'


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Position')

    class Meta:
        verbose_name_plural = 'Positions'

    def __str__(self) -> str:
        return f'{self.name}'


class Adress(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='adresses')
    street = models.CharField(max_length=30)
    house_number = models.PositiveSmallIntegerField()
    office_number = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Adresses'

    def __str__(self) -> str:
        if self.office_number:
            return f'{self.city}-{self.street}-{self.house_number}-{self.office_number}'
        else:
            return f'{self.city}-{self.street}-{self.house_number}'


class EmployeesNumber(models.Model):
    size_range = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Employees numbers'

    def __str__(self) -> str:
        return f'{self.size_range}'


class Sector(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Sector')

    class Meta:
        verbose_name_plural = 'Sectors'

    def __str__(self) -> str:
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Company name')
    employees_number = models.ForeignKey(
        EmployeesNumber,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='companies',
    )
    founded_in = models.PositiveSmallIntegerField()
    logo = models.ImageField(upload_to='image/logo/', null=True, blank=True)
    description = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    web_site = models.URLField()
    adress = models.OneToOneField(
        Adress, on_delete=models.SET_NULL, null=True, blank=True
    )
    sectors = models.ManyToManyField(Sector, related_name='companies_sectors')
    registred_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return f'{self.name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='employees'
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=35)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees'
    )
    image = models.ImageField(upload_to='image/avatar/', null=True, blank=True)
    positions = models.ManyToManyField(Position, related_name='employees_positions')
    registred_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.company.name}'


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Vacancy name')
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='vacancies'
    )
    description = models.TextField()
    salary = models.ForeignKey(
        Salary,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vacancies',
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='vacancies'
    )
    registred_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    countries = models.ManyToManyField(Country, related_name='vacancies_countries')
    contracts = models.ManyToManyField(Contract, related_name='vacancies_contracts')
    levels = models.ManyToManyField(Level, related_name='vacancies_levels')
    work_formats = models.ManyToManyField(
        WorkFormat, related_name='vacancies_work_formats'
    )
    tags = models.ManyToManyField(Tag, related_name='vacancies_tags')
    years_exp = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], default=0
    )

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self) -> str:
        return f'{self.name} in {self.company.name}'


class Review(models.Model):
    text = models.CharField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='reviews'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('user', 'company')
        verbose_name_plural = 'Reviews'

    def __str__(self) -> str:
        return f'From {self.user.username} to {self.company.name}'


class ReviewRating(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('review', 'user')
        verbose_name_plural = 'Reviews ratings'

    def __str__(self) -> str:
        return f'{self.rating.name} from {self.user.username} to {self.review.pk}'


class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='social_links',
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='social_links',
    )

    class Meta:
        verbose_name_plural = 'Social links'

    def __str__(self) -> str:
        if self.profile:
            return f'{self.profile.user.username} - {self.platform}'
        else:
            return f'{self.company.name} - {self.platform}'


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses')
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='responses'
    )
    text = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='responses',
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Responses'

    def __str__(self) -> str:
        return (
            f'{self.user.username} - {self.vacancy.name} to {self.vacancy.company.name}'
        )
