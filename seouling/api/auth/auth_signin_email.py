from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
import hashlib
from utils.helper import create_token
from api.auth.serializer import UserSerializer


class SigninEmail(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        password = hashlib.sha256(password.encode()).hexdigest()

        try:
            user = User.objects.get(email=email)

        except ObjectDoesNotExist:
            return Response(status=404, data={'message': '존재하지 않는 계정입니다.'})

        if user.password != password:
            return Response(status=404, data={'message': '비밀번호가 옳지 않습니다.'})

        user.token = create_token()
        user.save()

        return Response(status=200, data={'data': UserSerializer(user).data})
