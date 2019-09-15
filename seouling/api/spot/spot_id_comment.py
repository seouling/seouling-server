from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Comment
from api.spot.serializer import CommentSerializer
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer


class SpotIdCommentView(APIView):

    def get(self, request, spot_id):
        page = request.query_params.get('page', 1)
        comment_query = Comment.objects.filter(spot_id=spot_id)
        paginator = Paginator(comment_query, 10)
        page = paginator.page(page)
        page.count = paginator.count
        page.per_page = paginator.per_page

        result = dict()
        result['data'] = CommentSerializer(page.object_list, many=True).data
        result['paging'] = PageSerializer(page, context={'request': request}).data

        return Response(status=200, data=result)
