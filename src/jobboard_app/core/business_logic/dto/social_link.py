from dataclasses import dataclass


@dataclass
class AddSocialLinkDTO:
    platform: str | None
    url: str | None
