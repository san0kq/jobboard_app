from typing import Any, Optional

from core.models import Status
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.timezone import now

from .base import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        to="auth.User", primary_key=True, on_delete=models.CASCADE, related_name="profile"
    )
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(
        to="Gender",
        on_delete=models.SET_NULL,
        null=True,
        related_name="profiles",
        related_query_name="profile",
    )
    city = models.ForeignKey(
        to="City", on_delete=models.SET_NULL, null=True, related_name="profiles", related_query_name="profile"
    )
    avatar = models.ImageField(upload_to="image/avatar/", null=True, blank=True)
    resume = models.FileField(upload_to="resume/", null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    years_exp = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], null=True, blank=True, verbose_name="Years experience"
    )
    status = models.ForeignKey(
        to="core.Status",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profiles",
        related_query_name="profile",
    )
    work_format = models.ForeignKey(
        to="core.WorkFormat",
        on_delete=models.SET_NULL,
        null=True,
        related_name="profiles",
        related_query_name="profile",
    )
    level = models.ForeignKey(
        to="core.Level",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profiles",
        related_query_name="profile",
    )
    contract = models.ForeignKey(
        to="core.Contract",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profiles",
        related_query_name="profile",
    )
    salary = models.ForeignKey(
        to="core.Salary",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profiles",
        related_query_name="profile",
    )
    tags = models.ManyToManyField(to="core.Tag", related_name="profiles", related_query_name="profile")

    def get_default_profile_status(self) -> Any:
        return Status.objects.get_or_create(name='Open to work')[0]

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.status:
            self.status = self.get_default_profile_status()
        super().save(*args, **kwargs)

    def age(self) -> Optional[int]:
        """
        Calculate the age of the user.
        """
        if not self.birthday:
            return None
        n, b = now().date(), self.birthday
        return int(n.year - b.year - (0 if n.month > b.month or n.month == b.month and n.day >= b.day else 1))

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return f"ID: {self.pk} - {self.user.username}. Age: {self.age()}"
