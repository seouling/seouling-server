from django.urls import path
from api.spot.spot_id import SpotIdView

urlpatterns = [
    path('spot/<int:spot_id>', SpotIdView.as_view()),
]
