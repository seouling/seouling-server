from rest_framework import serializers
from api.models import Schedule
from api.spot.serializer import SpotSimpleSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    morning = SpotSimpleSerializer(many=True)
    after_noon = SpotSimpleSerializer(many=True)
    night = SpotSimpleSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('id', 'date', 'morning', 'after_noon', 'night')
