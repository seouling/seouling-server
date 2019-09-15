from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'password', 'token', 'sns_token', 'is_authenticated')


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'token', 'sns_token', 'is_push', 'last_login',
                   'created_at', 'is_authenticated', 'login_type')
