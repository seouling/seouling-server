from django.urls import path
from api.me.me import MyPageView


urlpatterns = [
    path('me', MyPageView.as_view())
]
