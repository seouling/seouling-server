from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Spot
from api.spot.serializer import SpotSerializer
from rest_framework.exceptions import NotFound
from django.db.models import Count


class SpotIdView(APIView):

    def get(self, request, spot_id):
        try:
            spot = Spot.objects.prefetch_related("pictures")\
                .annotate(like=Count('likes'), visitor=Count('visits')).get(id=spot_id)
        except Spot.DoesNotExist:
            raise NotFound('해당 id로 찾을 수 없습니다.')

        locale = request.META.get('HTTP_LOCALE')
        return Response(status=200, data={'data': SpotSerializer(spot, context={'locale': locale}).data})
