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
            add_list = value.get('add', [])
            remove_list = value.get('remove', [])

            for item in add_list:
                getattr(schedule, key).add(item)

            for item in remove_list:
                getattr(schedule, key).remove(item)

        locale = request.META.get('HTTP_LOCALE')

        return Response(status=200, data={'data': ScheduleSerializer(schedule, context={'locale': locale}).data})
