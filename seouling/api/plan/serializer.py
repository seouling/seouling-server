from rest_framework import serializers
from api.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, obj):
        try:
            schedule = obj.schedules.first()
            morning_spot = schedule.morning.first()
            picture = morning_spot.pictures.first().picture
            return picture
        except AttributeError:
            return ""

    class Meta:
        model = Plan
        fields = ('id', 'name', 'picture', 'created_at',
                  'start_date', 'end_date')
