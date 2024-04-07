import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Routine
from .models import WorkOuts

logger = logging.getLogger("django")
LOG = logger.info


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "name",
        ]


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = [
            "work_date",
            "works_json",
            "author_id",
        ]


class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOuts
        fields = "__all__"
