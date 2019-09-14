from rest_framework import serializers
from api.models import Spot


class SpotSerializer(serializers.ModelSerializer):
    visitor = serializers.IntegerField()
    like = serializers.IntegerField()

    class Meta:
        model = Spot
        fields = ('id', 'name', 'content', 'pictures', 'like', 'visitor')
