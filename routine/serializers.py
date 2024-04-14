import logging

from rest_framework import serializers
from .models import Routine, RoutineInfo
from .models import WorkOut

logger = logging.getLogger("django")
LOG = logger.info


class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOut
        fields = ["id", "workname", "work_type", "work_img", "work_video"]


class RoutineInfoSerializer(serializers.ModelSerializer):
    workout_name = serializers.ReadOnlyField(source="workout.work_name")
    workout_img = serializers.SerializerMethodField()

    class Meta:
        model = RoutineInfo
        fields = [
            "info_json",
            "workout",
            "workout_name",
            "workout_img",
            "routine_id",
            "id",
        ]

    def get_workout_img(self, obj):
        # obj의 workout 인스턴스가 존재하고 work_img가 있는 경우에만 반환
        if obj.workout and obj.workout.work_img:
            return obj.workout.work_img.url
        return None


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = ["routine_name", "user_id", "id"]
