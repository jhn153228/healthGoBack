from django.db import models

from accounts.models import User


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine_name = models.CharField(max_length=500)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.routine_name


class WorkOut(models.Model):
    work_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    work_type = models.CharField(max_length=50, null=False, blank=False)
    work_img = models.ImageField(null=True, blank=True)
    work_video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_name

    class Meta:
        ordering = ["-id"]


class RoutineInfo(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    workout = models.ForeignKey(WorkOut, on_delete=models.CASCADE)
    info_json = models.JSONField(default=dict)
