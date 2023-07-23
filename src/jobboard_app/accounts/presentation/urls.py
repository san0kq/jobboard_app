from accounts.presentation.views import ProfileView
from django.urls import path

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
]
