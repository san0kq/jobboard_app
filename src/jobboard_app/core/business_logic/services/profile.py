from logging import getLogger

from accounts.models import Profile

logger = getLogger(__name__)


def get_profile_by_pk(pk: int) -> Profile:
    profile: Profile = (
        Profile.objects.select_related(
            "user", "gender", "city", "status", "work_format", "level", "contract", "salary"
        )
        .prefetch_related("tags")
        .get(pk=pk)
    )

    logger.info("Successfully got profile.", extra={"profile_id": pk})

    return profile
