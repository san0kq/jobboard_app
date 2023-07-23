from typing import Any

from accounts.models import Profile


def get_profile_by_pk(pk: int) -> Any:
    profile = (
        Profile.objects.select_related(
            "user", "gender", "city", "status", "work_format", "level", "contract", "salary"
        )
        .prefetch_related("tags")
        .get(pk=pk)
    )

    return profile
