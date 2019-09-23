from django.urls import path
from api.search.search_tag import SearchTag
from api.search.search_name import SearchName


urlpatterns = [
    path('spot/search/name', SearchName.as_view()),
    path('spot/search/tag', SearchTag.as_view()),
]
