from django.conf import settings
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Routine(TimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work_date = models.DateField(null=False, blank=False)
    works_json = models.CharField(max_length=1000, null=False, blank=False)

    class Meta:
        ordering = ["-id"]


class WorkOuts(TimestampedModel):
    work_name = models.CharField(max_length=50, null=False, blank=False)
    work_type = models.CharField(max_length=50, null=False, blank=False)
    work_img = models.URLField(null=True, blank=True)
    work_video = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
