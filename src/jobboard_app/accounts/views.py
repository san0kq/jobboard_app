from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import render
from django.views import View

from .models import Profile

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


class ProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        profile = Profile.objects.get(pk=1)
        context = {"profile": profile}
        return render(request, "profile.html", context=context)
