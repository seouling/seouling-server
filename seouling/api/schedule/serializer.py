from rest_framework import serializers
from api.models import Schedule
from api.spot.serializer import SpotSimpleSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    morning = serializers.SerializerMethodField()
    after_noon = serializers.SerializerMethodField()
    night = serializers.SerializerMethodField()

    def get_morning(self, obj):
        return SpotSimpleSerializer(obj.morning, many=True, context={'locale': self.context['locale']}).data

    def get_after_noon(self, obj):
        return SpotSimpleSerializer(obj.after_noon, many=True, context={'locale': self.context['locale']}).data

    def get_night(self, obj):
        return SpotSimpleSerializer(obj.night, many=True, context={'locale': self.context['locale']}).data

    class Meta:
        model = Schedule
        fields = ('id', 'date', 'morning', 'after_noon', 'night')
