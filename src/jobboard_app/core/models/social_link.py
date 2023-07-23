from django.db import models

from .base import BaseModel


class SocialLink(BaseModel):
    platform = models.CharField(max_length=100)
    url = models.URLField(
        max_length=200,
        error_messages={"invalid": "Invalid URL. Example: https://www.job-board.by"},
    )
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="social_links",
        related_query_name="social_link",
    )
    company = models.ForeignKey(
        to="Company",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="social_links",
        related_query_name="social_link",
    )

    class Meta:
        verbose_name_plural = "Social links"

    def __str__(self) -> str:
        if self.profile:
            return f"{self.profile.user.username} - {self.platform}"
        else:
            return f"{self.company.name} - {self.platform}"
