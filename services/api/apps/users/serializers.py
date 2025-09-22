from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "admission_number",
            "department",
            "school",
            "is_student",
        ]

