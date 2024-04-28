from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])

        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "login_id",
            "password",
            "username",
            "email",
            "spec_json",
        ]
