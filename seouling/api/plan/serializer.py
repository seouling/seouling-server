from rest_framework import serializers
from api.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    scheme = serializers.SerializerMethodField()

    def get_picture(self, obj):
        schedule = obj.schedules.first()
        morning_spot = schedule.morning.first()
        picture = morning_spot.pictures.first().picture
        return picture

    def get_scheme(self, obj):
        return f"seoul://plan/{obj.id}"

    class Meta:
        model = Plan
        fields = ('id', 'scheme', 'name', 'picture', 'created_at',
                  'start_date', 'end_date')
