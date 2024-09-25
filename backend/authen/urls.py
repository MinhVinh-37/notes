from authen.views import (
    CallbackGoogleLoginView,
    LoginInitState,
    LogoutView,
    RedirectGoogleLoginView,
)
from django.urls import path

urlpatterns = [
    path(
        "google/redirect",
        RedirectGoogleLoginView.as_view(),
        name="google-oauth2-redirect",
    ),
    path(
        "google/callback",
        CallbackGoogleLoginView.as_view(),
        name="google-oauth2-callback",
    ),
    path(
        "logout",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "google/init_state",
        LoginInitState.as_view(),
        name="login-init-state",
    ),
]
