from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Visit


class SpotIdVisitView(APIView):

    def post(self, request, spot_id):
        try:
            Visit.objects.get(spot_id=spot_id, user=request.user)
        except Visit.DoesNotExist:
            visit = Visit(spot_id=spot_id, user=request.user)
            visit.save()

        return Response(status=200, data={'message': 'success'})
