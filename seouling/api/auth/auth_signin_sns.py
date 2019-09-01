from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from utils.helper import create_token


class SigninSNS(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        sns_token = request.data.get('sns_token')
        try:
            user = User.objects.get(sns_token=sns_token)

        except ObjectDoesNotExist:
            return Response(status=404, data={'message': '존재하지 않는 계정입니다.'})

        user.token = create_token()
        user.save()
        return Response(status=200, data={'token': user.token})
