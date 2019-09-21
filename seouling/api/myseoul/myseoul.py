from rest_framework.views import APIView
from rest_framework.response import Response
from api.spot.serializer import SpotMySeoulSerializer
from api.models import Spot
from rest_framework.exceptions import ParseError


class MySeoulView(APIView):
    def get(self, request):
        gu = request.query_params.get('gu')
        if gu is None:
            raise ParseError('구를 입력해주세요.')

        amount_count = Spot.objects.count()
        visit_count = request.user.visits.count()

        checked_spots = Spot.objects.filter(gu=gu, visits__user_id=request.user).all()
        not_checked_spots = Spot.objects.filter(gu=gu, visits__user_id=None).all()

        return Response(status=200, data={'data': {
            'checked': SpotMySeoulSerializer(checked_spots, many=True).data,
            'not_checked': SpotMySeoulSerializer(not_checked_spots, many=True).data,
            'amount_count': amount_count,
            'visit_count': visit_count
        }})
