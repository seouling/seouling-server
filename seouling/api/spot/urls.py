from django.urls import path
from api.spot.spot_id import SpotIdView
from api.spot.spot_id_comment import SpotIdCommentView
from api.spot.spot_id_like import SpotIdLikeView
from api.spot.spot_id_visit import SpotIdVisitView


urlpatterns = [
    path('spot/<int:spot_id>', SpotIdView.as_view()),
    path('spot/<int:spot_id>/comment', SpotIdCommentView.as_view()),
    path('spot/<int:spot_id>/like', SpotIdLikeView.as_view()),
    path('spot/<int:spot_id>/visit', SpotIdVisitView.as_view()),
]
