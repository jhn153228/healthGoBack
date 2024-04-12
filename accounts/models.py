from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, login_id, password=None):
        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email), login_id=login_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, login_id, password):
        user = self.create_user(
            email=self.normalize_email(email), login_id=login_id, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    login_id = models.CharField(max_length=20, null=False, unique=True)
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    spec_json = models.JSONField("json", default=dict, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "login_id"
    REQUIRED_FIELDS = ["email"]
