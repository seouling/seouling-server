from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Spot
from api.spot.serializer import SpotCoordinateSerializer


class SpotCoordinateView(APIView):

    def get(self, _):
        spots = Spot.objects.values('id', 'lat', 'lng').all()
        return Response(status=200, data={'data': SpotCoordinateSerializer(spots, many=True).data})
