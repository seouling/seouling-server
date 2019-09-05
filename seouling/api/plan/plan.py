from rest_framework.views import APIView
from rest_framework.response import Response
from api.plan.serializer import PlanSerializer
from utils.helper import get_after_url
from api.models import Plan, Schedule


class PlanView(APIView):

    def get(self, request):
        last_id = request.query_params.get('last_id')

        plan_query = Plan.objects.filter(user_id=request.user.id)
        if last_id is not None:
            plan_query = plan_query.filter(id__lt=last_id)

        last_plan = plan_query.values('id').order_by('-id').last()
        plans = plan_query.order_by('-id')[:10]

        result = dict()
        result['data'] = PlanSerializer(plans, many=True).data
        result['paging'] = {"after": get_after_url('/plan', last_plan['id'])} if last_plan is not None else {}

        return Response(status=200, data=result)
