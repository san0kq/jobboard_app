from typing import Optional

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Tag')

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return f'{self.name}'


class Gender(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Gender')

    class Meta:
        verbose_name_plural = 'Genders'

    def __str__(self) -> str:
        return f'{self.name}'


class Language(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Language')

    class Meta:
        verbose_name_plural = 'Languages'

    def __str__(self) -> str:
        return f'{self.name}'


class LanguageLevel(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Language level')

    class Meta:
        verbose_name_plural = 'Language levels'

    def __str__(self) -> str:
        return f'{self.name}'


class WorkFormat(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Work format')

    class Meta:
        verbose_name_plural = 'Work formats'

    def __str__(self) -> str:
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Status')

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self) -> str:
        return f'{self.name}'


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Country')

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City')
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities'
    )

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self) -> str:
        return f'{self.name} - {self.country.name}'


class Contract(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Contract')

    class Meta:
        verbose_name_plural = 'Contracts'

    def __str__(self) -> str:
        return f'{self.name}'


class Level(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Level')

    class Meta:
        verbose_name_plural = 'Levels'

    def __str__(self) -> str:
        return f'{self.name}'


class Salary(models.Model):
    min_salary = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    max_salary = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    class Meta:
        unique_together = ('min_salary', 'max_salary')
        verbose_name_plural = 'Salaries'

    def __str__(self) -> str:
        return f'{self.min_salary} - {self.max_salary}'


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name='profile'
    )
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    image = models.ImageField(upload_to='image/avatar/', null=True, blank=True)
    resume = models.TextField()
    years_exp = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], null=True, blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        default=1,
    )
    work_format = models.ForeignKey(
        WorkFormat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
    )
    level = models.ForeignKey(
        Level, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    contract = models.ForeignKey(
        Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    salary = models.ForeignKey(
        Salary, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    tags = models.ManyToManyField(Tag, related_name='profiles_tags')

    def age(self) -> Optional[int]:
        """
        Calculate the age of the user.
        """
        if not self.birthday:
            return None
        n, b = now().date(), self.birthday
        return int(
            n.year
            - b.year
            - (0 if n.month > b.month or n.month == b.month and n.day >= b.day else 1)
        )

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return f'ID: {self.pk} - {self.user.username}. Age: {self.age()}'


class ProfileLanguage(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='languages'
    )
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name='languages'
    )
    language_level = models.ForeignKey(
        LanguageLevel, on_delete=models.CASCADE, related_name='languages'
    )

    class Meta:
        verbose_name_plural = 'Profile languages'

    def __str__(self) -> str:
        return f'{self.profile.user.username} - {self.language.name} - {self.language_level.name}'
