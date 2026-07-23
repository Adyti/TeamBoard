from django.contrib.auth.models import User
from rest_framework import serializers
from .models import KBEntry


class RegisterSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "company_name",
        ]

    def create(self, validated_data):
        company_name = validated_data.pop("company_name")

        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )

        user.company.company_name = company_name
        user.company.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class KBEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = KBEntry
        fields = [
            "id",
            "question",
            "answer",
            "category",
        ]