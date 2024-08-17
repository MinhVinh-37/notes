import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, uuid, email, oauth2_provider, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not uuid:
            raise ValueError("Users must have an email address")

        user = self.model(
            uuid=uuid,
            email=self.normalize_email(email),
            oauth2_provider=oauth2_provider,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uuid, email, oauth2_provider, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            uuid,
            email,
            oauth2_provider,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "user"
        db_table = "user"
        unique_together = ("email", "oauth2_provider")

    USERNAME_FIELD = "uuid"
    REQUIRED_FIELDS = ["email", "oauth2_provider"]

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
    )
    access_token = models.CharField(
        max_length=255,
    )
    expires_in = models.DateTimeField()
    refresh_token = models.CharField(
        max_length=255,
    )
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
    )
    oauth2_provider = models.CharField(
        max_length=20,
        default="notes",
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email
