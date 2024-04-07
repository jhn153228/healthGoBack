from django.contrib import admin
from .models import Routine, WorkOuts


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkOuts)
class WorkOutsAdmin(admin.ModelAdmin):
    pass
