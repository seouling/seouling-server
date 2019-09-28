from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Spot, SpotTag
from api.spot.serializer import SpotSimpleSerializer
from django.db import models
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer
from django.db.models import Subquery, OuterRef
from utils.gu import kr_gu


class SQCount(Subquery):
    template = "(SELECT count(*) FROM (%(subquery)s) _count)"
    output_field = models.IntegerField()


class SearchTag(APIView):

    def post(self, request):
        gu = request.data.get('gu', [])
        tags = request.data.get('tags', [])
        page = request.query_params.get('page', 1)

        if len(tags) == 0:
            tags = [-1]

        if len(gu) == 0:
            spot_query = Spot.objects.all()

        else:
            spot_query = Spot.objects.filter(gu__in=gu)

        spot_query = spot_query.annotate(
                rank=SQCount(SpotTag.objects.filter(spot_id=OuterRef("pk"), tag_id__in=tags).values('pk'))
            ).order_by('-rank')

        paginator = Paginator(spot_query, 10)
        page = paginator.page(page)
        page.count = paginator.count
        page.per_page = paginator.per_page

        locale = request.META.get('HTTP_LOCALE')
        result = dict()
        result['data'] = SpotSimpleSerializer(page.object_list, many=True, context={'locale': locale}).data
        result['paging'] = PageSerializer(page, context={'request': request}).data
        return Response(status=200, data=result)
