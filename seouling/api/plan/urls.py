from django.urls import path
from api.plan.plan import PlanView

urlpatterns = [
    path('', PlanView.as_view()),
]
