from rest_framework.views import APIView
from rest_framework.response import Response
from api.schedule.serializer import ScheduleSerializer
from api.models import Schedule
from rest_framework.exceptions import NotFound


class ScheduleIdView(APIView):

    def put(self, request, schedule_id):
        try:
            schedule = Schedule.objects.get(plan_id=schedule_id)
        except Schedule.DoesNotExist:
            raise NotFound('해당 id로 찾을 수 없습니다.')

        type = request.data.get('type')
        add_list = request.data.get('add', [])
        remove_list = request.data.get('remove', [])

        if type is None:
            return Response(status=400, data={'message': 'type을 설정해주세요.'})

        for item in add_list:
            getattr(schedule, type).add(item)

        for item in remove_list:
            getattr(schedule, type).remove(item)

        return Response(status=200, data={'data': ScheduleSerializer(schedule).data})
