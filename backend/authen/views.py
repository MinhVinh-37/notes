from datetime import datetime, timedelta

import jwt
from accounts.models import User
from authen.serializers import CallbackGoogleLoginSerializer
from authen.services.google import GoogleOauth2Service
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class LoginInitState(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request: Request) -> Response:
        state = GoogleOauth2Service().generate_state()
        request.session["google_oauth2_state"] = state
        return Response(
            {
                "state": state,
            }
        )


class RedirectGoogleLoginView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request: Request):
        authorization_url, state = GoogleOauth2Service().get_authorization_url()
        request.session["google_oauth2_state"] = state
        return redirect(authorization_url)


class CallbackGoogleLoginView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CallbackGoogleLoginSerializer

    def get(self, request: Request):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        tokens = GoogleOauth2Service().get_tokens(validated_data["code"])

        user_info = jwt.decode(tokens["id_token"], options={"verify_signature": False})
        email = user_info["email"]
        user, _ = User.objects.get_or_create(
            email=email,
            oauth2_provider="google",
            defaults={
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"],
                "expires_in": datetime.now() + timedelta(seconds=tokens["expires_in"]),
            },
        )

        login(request, user)

        return redirect(reverse("notes-list"))


class LogoutView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        logout(request)
        return Response()
