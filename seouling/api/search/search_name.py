from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Spot
from api.spot.serializer import SpotSimpleSerializer
from rest_framework.exceptions import ParseError
from django.db.models import Q
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer


class SearchName(APIView):

    def post(self, request):
        name = request.data.get('name')
        # page = request.query_params.get('page', 1)
        if name is None:
            raise ParseError('검색어를 입력해주세요.')

        spot_query = Spot.objects.filter(Q(kr_name__contains=name) | Q(en_name__contains=name))\
            .prefetch_related('pictures').all()
        # paginator = Paginator(spot_query, 10)
        # page = paginator.page(page)
        # page.count = paginator.count
        # page.per_page = paginator.per_page

        locale = request.META.get('HTTP_LOCALE')
        result = dict()
        result['data'] = SpotSimpleSerializer(spot_query, many=True, context={'locale': locale}).data
        # result['paging'] = PageSerializer(page, context={'request': request}).data
        return Response(status=200, data=result)
