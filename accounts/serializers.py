import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger("django")


class SignupSerializer(serializers.ModelSerializer):
    logging.info("testsetse")
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            **validated_data
            # username=validated_data["username"],
            # bench_1rm=validated_data["bench_1rm"],
            # squat_1rm=validated_data["squat_1rm"],
            # deadlift_1rm=validated_data["deadlift_1rm"],
        )
        user.set_password(validated_data["password"])

        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "password",
            "bench_1rm",
            "squat_1rm",
            "deadlift_1rm",
        ]
