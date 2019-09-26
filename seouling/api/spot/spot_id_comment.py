from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Comment
from api.spot.serializer import CommentSerializer
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer
from rest_framework.exceptions import ParseError


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

    def post(self, request, spot_id):
        content = request.data['content']
        score = request.data['score']

        if content is None:
            raise ParseError('내용을 입력해주세요.')

        if score is None:
            raise ParseError('별점을 입력해주세요.')

        comment = Comment(spot_id=spot_id, writer=request.user, content=content, score=score)
        comment.save()

        return Response(status=200, data={'message': CommentSerializer(comment)})
