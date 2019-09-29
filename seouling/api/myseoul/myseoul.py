from rest_framework.views import APIView
from rest_framework.response import Response
from api.spot.serializer import SpotMySeoulSerializer
from api.models import Spot


class MySeoulView(APIView):
    def get(self, request):
        locale = request.META.get('HTTP_LOCALE')
        if locale == 'ko':
            order = 'kr_name'
        else:
            order = 'en_name'

        checked_spots = Spot.objects.filter(visits__user_id=request.user).order_by(order).all()
        not_checked_spots = Spot.objects.exclude(visits__user_id=request.user).order_by(order).all()

        locale = request.META.get('HTTP_LOCALE')

        return Response(status=200, data={'data': {
            'checked': SpotMySeoulSerializer(checked_spots, many=True, context={"locale": locale}).data,
            'not_checked': SpotMySeoulSerializer(not_checked_spots, many=True, context={"locale": locale}).data
        }})
