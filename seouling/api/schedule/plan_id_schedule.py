from rest_framework.views import APIView
from rest_framework.response import Response
from api.schedule.serializer import ScheduleSerializer
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer
from api.models import Schedule


class PlanScheduleView(APIView):

    def get(self, request, plan_id):
        page = request.query_params.get('page', 1)

        schedule_query = Schedule.objects.filter(plan_id=plan_id).order_by('date')\
            .prefetch_related('morning', 'after_noon', "night")

        paginator = Paginator(schedule_query, 3)
        page = paginator.page(page)
        page.count = paginator.count
        page.per_page = paginator.per_page

        locale = request.META.get('HTTP_LOCALE')
        result = dict()
        result['data'] = ScheduleSerializer(page.object_list, many=True, context={"locale": locale}).data
        result['paging'] = PageSerializer(page, context={'request': request}).data

        return Response(status=200, data=result)
