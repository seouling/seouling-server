from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from api.me.serializer import UserSerializer
from django.db.models import Count


class MyPageView(APIView):

    def user(self, request_user):
        user = User.objects.annotate(my_seoul_count=Count('visits')).get(id=request_user.id)
        return Response(status=200, data={'data': UserSerializer(user).data})

    def get(self, request):
        return self.user(request.user)

    def put(self, request):
        profile_picture = request.data.get('profile_picture')
        is_push = request.data.get('is_push')
        nickname = request.data.get('nickname')

        if profile_picture is not None:
            request.user.profile_picture = profile_picture

        if is_push is not None:
            request.user.is_push = is_push

        if nickname is not None:
            request.user.profile_picture = nickname

        request.user.save()

        return self.user(request.user)

