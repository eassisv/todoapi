from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password"]
        read_only_fields = ["email", "first_name", "last_name"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "username": {"validators": []},
        }

    def validate(self, attrs):
        user = authenticate(self.context["request"], **attrs)
        if not user:
            raise serializers.ValidationError("invalid username or password")
        return {"user": user}

    def create(self, validated_data):
        return validated_data["user"]
