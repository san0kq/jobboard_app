from django.db import models

from .base import BaseModel


class ReviewRating(BaseModel):
    review = models.ForeignKey(
        to="Review", on_delete=models.CASCADE, related_name="ratings", related_query_name="rating"
    )
    user = models.ForeignKey(
        to="auth.User", on_delete=models.CASCADE, related_name="ratings", related_query_name="rating"
    )
    rating = models.ForeignKey(
        to="Rating", on_delete=models.CASCADE, related_name="reviews", related_query_name="review"
    )

    class Meta:
        unique_together = ("review", "user")
        verbose_name_plural = "Reviews ratings"

    def __str__(self) -> str:
        return f"{self.rating.name} from {self.user.username} to {self.review.pk}"
