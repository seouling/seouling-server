from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from rest_framework.permissions import AllowAny
import hashlib
from api.auth.serializer import UserSerializer
from rest_framework.exceptions import ParseError


class Signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        sns_token = request.data.get('sns_token')
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        profile_picture = request.data.get('profile_picture')
        login_type = request.data.get('login_type')

        if nickname is None:
            return Response(status=400, data={'message': '닉네임이 존재하지 않습니다.'})

        if sns_token is None and email is None:
            return Response(status=400, data={'message': '이메일 토큰 SNS 토큰이 없습니다.'})

        data = dict()
        data['nickname'] = nickname
        data['login_type'] = login_type

        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise ParseError('이미 존재하는 이메일입니다.')

        is_exists = User.objects.filter(nickname=nickname).exists()
        if is_exists:
            raise ParseError('이미 존재하는 닉네임입니다.')

        if login_type == 'facebook':
            # Todo: SNS 계정 체크
            pass

        if email is not None:
            data['email'] = email
            password = request.data.get('password')
            data['password'] = hashlib.sha256(password.encode()).hexdigest()

        if sns_token is not None:
            data['sns_token'] = sns_token

        if profile_picture is not None:
            data['profile_picture'] = profile_picture

        user = User(**data)
        user.save()
        return Response(status=200, data={'data': UserSerializer(user).data})
