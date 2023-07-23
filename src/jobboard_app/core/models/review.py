from django.db import models

from .base import BaseModel


class Review(BaseModel):
    text = models.TextField(max_length=800)
    user = models.ForeignKey(
        to="auth.User", on_delete=models.CASCADE, related_name="reviews", related_query_name="review"
    )
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, related_name="reviews", related_query_name="review"
    )

    class Meta:
        unique_together = ("user", "company")
        verbose_name_plural = "Reviews"

    def __str__(self) -> str:
        return f"From {self.user.username} to {self.company.name}"
