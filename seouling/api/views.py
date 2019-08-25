from rest_framework.views import APIView
from rest_framework.response import Response
from utils.authentication import TokenAuthentication


class TMP(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        return Response(status=200, data={'message': 'hi'})
