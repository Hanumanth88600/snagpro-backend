from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField()

    def validate(self, attrs):

        user = authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError({
    "message":
    "Invalid Username or Password"
})

        attrs["user"] = user

        return attrs
    
    
from accounts.models import User


class StaffCreateSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = (
            "first_name",
            "email",
            "phone",
            "role",
        )
 
class ProfileSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [

            "id",
            "username",
            "email",
            "first_name"

        ] 