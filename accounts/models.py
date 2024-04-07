from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    bench_1rm = models.IntegerField(null=True, blank=True)
    squat_1rm = models.IntegerField(null=True, blank=True)
    deadlift_1rm = models.IntegerField(null=True, blank=True)
