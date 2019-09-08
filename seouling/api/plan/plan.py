from rest_framework.views import APIView
from rest_framework.response import Response
from api.plan.serializer import PlanSerializer
from utils.page_serializer import PageSerializer
from api.models import Plan
from django.core.paginator import Paginator


class PlanView(APIView):

    def get(self, request):
        page = request.query_params.get('page', 1)

        plan_query = Plan.objects.filter(user_id=request.user.id).order_by('-id')

        paginator = Paginator(plan_query, 10)
        page = paginator.page(page)

        result = dict()
        result['data'] = PlanSerializer(page.object_list, many=True).data
        result['paging'] = PageSerializer(page, context={'request': request}).data

        return Response(status=200, data=result)


