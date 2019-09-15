from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    my_seoul_count = serializers.IntegerField()

    class Meta:
        model = User
        exclude = ('password', 'token', 'sns_token', 'is_authenticated')

