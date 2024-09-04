from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users import models


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'date_joined',
            'last_login',
        ]

