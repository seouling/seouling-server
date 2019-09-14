from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.plan.serializer import PlanSerializer
from api.models import Plan


class PlanIdView(APIView):

    def put(self, request, plan_id):
        data = request.data

        plan = Plan.objects.filter(id=plan_id)
        if not plan.exists():
            raise NotFound('해당 id로 찾을 수 없습니다.')

        plan.update(**data)

        result = dict()
        result['data'] = PlanSerializer(plan.first()).data

        return Response(status=200, data=result)

    def delete(self, _, plan_id):
        try:
            plan = Plan.objects.get(id=plan_id)
        except Plan.DoesNotExist:
            raise NotFound('해당 id로 찾을 수 없습니다.')

        plan.delete()
        return Response(status=204, data={'message': "정상적으로 삭제되었습니다."})
