from django.urls import path
from api.spot.spot_id import SpotIdView
from api.spot.spot_id_comment import SpotIdCommentView


urlpatterns = [
    path('spot/<int:spot_id>', SpotIdView.as_view()),
    path('spot/<int:spot_id>/comment', SpotIdCommentView.as_view()),
]
