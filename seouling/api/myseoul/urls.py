from django.urls import path
from api.myseoul.myseoul import MySeoulView

urlpatterns = [
    path('myseoul', MySeoulView.as_view())
]
