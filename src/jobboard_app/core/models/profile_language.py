from django.db import models

from .base import BaseModel


class ProfileLanguage(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="languages",
        related_query_name="language",
    )
    language = models.ForeignKey(
        to="Language", on_delete=models.CASCADE, related_name="profiles", related_query_name="profile"
    )
    language_level = models.ForeignKey(
        to="LanguageLevel",
        on_delete=models.CASCADE,
        related_name="+",
    )

    class Meta:
        unique_together = ("profile", "language")
        verbose_name_plural = "Profile languages"

    def __str__(self) -> str:
        return f"{self.profile.user.username} - {self.language.name} - {self.language_level.name}"
