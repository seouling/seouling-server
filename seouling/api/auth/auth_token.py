from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist


class CheckToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            User.objects.get(token=request.data['token'])

        except ObjectDoesNotExist:
            return Response(status=400, data={'message': '사용할 수 없는 토큰입니다.'})

        return Response(status=200, data={'message': '사용 가능한 토큰입니다.'})
