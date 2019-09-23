from django.urls import path, include
from api.views import Parsing

urlpatterns = [
    path('', include('api.plan.urls')),
    path('', include('api.auth.urls')),
    path('', include('api.schedule.urls')),
    # path('', include('api.tag.urls')),
    path('', include('api.spot.urls')),
    path('', include('api.me.urls')),
    path('', include('api.myseoul.urls')),
    path('', include('api.search.urls')),
    path('parsing', Parsing.as_view()),
]
