from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CallbackGoogleLoginSerializer(serializers.Serializer):
    state = serializers.CharField(required=False)
    code = serializers.CharField(required=False)
    error = serializers.CharField(required=False)

    def validate_state(self, value):
        request = self.context["request"]
        if value != request.session.get("google_oauth2_state", None):
            raise ValidationError(
                detail="Check CSRF fail",
                code="csrf_error",
            )

        return value

    def validate(self, attrs):
        if "error" not in attrs:
            if attrs["code"] is None or attrs["state"] is None:
                raise ValidationError(
                    detail="Code and state are required if don't have error.",
                    code="required",
                )

        return super().validate(attrs)
