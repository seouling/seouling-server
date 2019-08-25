from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from rest_framework.permissions import AllowAny
import hashlib
from api.auth.serializer import UserSerializer
from utils.helper import upload_image_to_s3


class Signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        sns_token = request.data.get('sns_token')
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        profile_picture = request.FILES.get('profile_picture')
        login_type = request.data.get('login_type')

        if nickname is None:
            return Response(status=200, data={'message': '닉네임이 존재하지 않습니다.'})

        if sns_token is None and email is None:
            return Response(status=200, data={'message': '이메일 토큰 SNS 토큰이 없습니다.'})

        data = {}

        if login_type > 0:
            # Todo: SNS 계정 체크
            pass

        data['login_type'] = login_type
        if email is not None:
            data['email'] = email
            password = request.data.get('password')
            data['password'] = hashlib.sha256(password.encode()).hexdigest()

        if sns_token is not None:
            data['sns_token'] = sns_token

        if profile_picture is not None:
            data['profile_picture'] = upload_image_to_s3(profile_picture)

        user = User(**data)
        user.save()

        return Response(status=200, data={'data': UserSerializer(user).data})
