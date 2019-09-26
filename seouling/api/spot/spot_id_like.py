from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Like


class SpotIdLikeView(APIView):

    def post(self, request, spot_id):
        try:
            like = Like.objects.get(spot_id=spot_id, user=request.user)
            like.delete()

        except Like.DoesNotExist:
            like = Like(spot_id=spot_id, user=request.user)
            like.save()

        return Response(status=200, data={'message': 'success'})
