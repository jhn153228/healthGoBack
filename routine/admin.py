from django.contrib import admin

from routine.models import Routine, WorkOut, RoutineInfo


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkOut)
class WorkOutsAdmin(admin.ModelAdmin):
    pass


@admin.register(RoutineInfo)
class RoutineInfosAdmin(admin.ModelAdmin):
    pass
