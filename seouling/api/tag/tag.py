# from rest_framework.views import APIView
# from rest_framework.response import Response
# from api.models import Tag
# from api.tag.serializer import TagSerializer
#
#
# class TagView(APIView):
#
#     def get(self, _):
#         tags = Tag.objects.all()
#
#         return Response(status=200, data={'data': TagSerializer(tags, many=True).data})
