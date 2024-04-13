import logging

from rest_framework import serializers
from .models import Routine, RoutineInfo
from .models import WorkOut

logger = logging.getLogger("django")
LOG = logger.info


class RoutineInfoSerializer(serializers.ModelSerializer):
    workout_name = serializers.SerializerMethodField()

    class Meta:
        model = RoutineInfo
        fields = ["info_json", "workout", "workout_name", "routine_id", "id"]

    def get_workout_name(self, obj):
        # obj.workout_id는 workout_id의 값을 의미합니다.
        # 해당 workout_id에 해당하는 Workout 모델 인스턴스를 가져와서 workout_name을 반환합니다.
        workout_id = obj.workout_id
        workout = WorkOut.objects.get(pk=workout_id)
        return workout.work_name


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = ["routine_name", "user_id", "id"]


class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOut
        fields = "__all__"
