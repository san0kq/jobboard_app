from __future__ import annotations

from typing import TYPE_CHECKING

from core.business_logic.services import get_profile_by_pk
from django.shortcuts import render
from django.views import View

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


class ProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        profile = get_profile_by_pk(pk=1)
        context = {"profile": profile}
        return render(request, "profile.html", context=context)
