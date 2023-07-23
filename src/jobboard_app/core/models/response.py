from typing import Any

from django.db import models

from .base import BaseModel
from .status import Status


class Response(BaseModel):
    user = models.ForeignKey(
        to="auth.User", on_delete=models.CASCADE, related_name="responses", related_query_name="response"
    )
    vacancy = models.ForeignKey(
        to="Vacancy", on_delete=models.CASCADE, related_name="responses", related_query_name="response"
    )
    text = models.CharField(max_length=500)
    resume = models.FileField(upload_to="resume/", null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    status = models.ForeignKey(
        to="Status",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="responses",
        related_query_name="response",
    )

    class Meta:
        verbose_name_plural = "Responses"

    def get_default_response_status(self) -> Any:
        return Status.objects.get_or_create(name='Created')[0]

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.status:
            self.status = self.get_default_response_status()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.vacancy.name} to {self.vacancy.company.name}"
