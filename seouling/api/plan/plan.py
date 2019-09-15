from rest_framework.views import APIView
from rest_framework.response import Response
from api.plan.serializer import PlanSerializer
from utils.page_serializer import PageSerializer
from api.models import Plan, Schedule
from django.core.paginator import Paginator
import datetime
from utils.helper import daterange
from django.db import transaction
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema

# plan_response = openapi.Response('response description', PlanSerializer)
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)


class PlanView(APIView):
    # @swagger_auto_schema(manual_parameters=[test_param], responses={200: plan_response})
    def get(self, request):
        page = request.query_params.get('page', 1)

        # Todo: 쿼리 최적화 필요
        plan_query = Plan.objects.filter(user_id=request.user.id).order_by('-id').prefetch_related('schedules')

        paginator = Paginator(plan_query, 10)
        page = paginator.page(page)
        page.per_page = paginator.per_page
        page.count = paginator.count

        result = dict()
        result['data'] = PlanSerializer(page.object_list, many=True).data
        result['paging'] = PageSerializer(page, context={'request': request}).data

        return Response(status=200, data=result)

    def post(self, request):
        name = request.data.get('name')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        if name is None:
            return Response(status=400, data={"message": "여행 제목을 입력해주세요"})

        if start_date is None:
            return Response(status=400, data={"message": "시작 날짜를 입력해주세요"})

        if end_date is None:
            return Response(status=400, data={"message": "종료 날짜를 입력해주세요"})

        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        with transaction.atomic():
            plan = Plan(user=request.user, name=name, start_date=start_date, end_date=end_date)
            plan.save()

            for date in daterange(start_date, end_date):
                schedule = Schedule(plan_id=plan.id, date=date)
                schedule.save()

        result = dict()
        result['data'] = PlanSerializer(plan).data

        return Response(status=200, data=result)
