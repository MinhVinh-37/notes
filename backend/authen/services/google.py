import os
from random import SystemRandom
from urllib.parse import urlencode

import requests
from attrs import define
from django.urls import reverse
from oauthlib.common import UNICODE_ASCII_CHARACTER_SET
from requests import Response


@define
class GoogleOauth2Env:
    GOOGLE_OAUTH2_CLIENT_ID = os.getenv("GOOGLE_OAUTH2_CLIENT_ID", None)
    GOOGLE_OAUTH2_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH2_CLIENT_SECRET", None)


class GoogleOauth2Service:
    def __init__(self) -> None:
        self.host = "https://accounts.google.com/o/oauth2/v2/auth"
        self.token_host = "https://oauth2.googleapis.com/token"
        self.client_id = GoogleOauth2Env.GOOGLE_OAUTH2_CLIENT_ID
        self.client_secret = GoogleOauth2Env.GOOGLE_OAUTH2_CLIENT_SECRET
        self.scopes = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "openid",
        ]
        self.redirect_uri = f"http://127.0.0.1:8000{reverse('google-oauth2-callback')}"

    def _generate_state(self) -> str:
        rand = SystemRandom()
        state = "".join([rand.choice(UNICODE_ASCII_CHARACTER_SET) for _ in range(30)])
        return state

    def get_authorization_url(self) -> tuple[str, str]:
        scopes = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email",
            "openid",
        ]
        state = self._generate_state()

        request_params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": " ".join(scopes),
            "state": state,
            "access_type": "offline",
            "include_granted_scopes": "true",
            "prompt": "select_account",
        }

        query_params = urlencode(request_params)
        authorization_url = f"{self.host}?{query_params}"

        return authorization_url, state

    def get_tokens(self, code: str) -> tuple[str, str]:
        request_body = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
        }
        response: Response = requests.post(self.token_host, json=request_body)
        return response.json()
