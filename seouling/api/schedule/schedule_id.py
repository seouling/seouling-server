from rest_framework.views import APIView
from rest_framework.response import Response
from api.schedule.serializer import ScheduleSerializer
from api.models import Schedule
from rest_framework.exceptions import NotFound


class ScheduleIdView(APIView):

    def put(self, request, schedule_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            raise NotFound('해당 id로 찾을 수 없습니다.')

        for key, value in request.data.items():
            getattr(schedule, key).clear()
            for spot in value:
                getattr(schedule, key).add(spot)

        locale = request.META.get('HTTP_LOCALE')

        return Response(status=200, data={'data': ScheduleSerializer(schedule, context={'locale': locale}).data})
