from rest_framework import serializers
from api.models import Spot, Comment
from api.auth.serializer import UserSimpleSerializer


class SpotSerializer(serializers.ModelSerializer):
    visitor = serializers.IntegerField()
    like = serializers.IntegerField()

    class Meta:
        model = Spot
        fields = ('id', 'name', 'content', 'pictures', 'like', 'visitor')


class SpotSimpleSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, obj):
        return obj.pictures.first()

    class Meta:
        model = Spot
        fields = ('id', 'name', 'content', 'picture')


class CommentSerializer(serializers.ModelSerializer):
    writer = UserSimpleSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'writer')
