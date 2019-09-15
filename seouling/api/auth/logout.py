from rest_framework.views import APIView
from rest_framework.response import Response
from utils.helper import create_token


class Logout(APIView):

    def post(self, request):
        request.user.token = create_token()
        request.user.save()

        return Response(status=200, data={'message': '로그아웃 되었습니다.'})
