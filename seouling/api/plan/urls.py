from django.urls import path
from api.plan.plan import PlanView
from api.plan.plan_id import PlanIdView

urlpatterns = [
    path('plan/', PlanView.as_view()),
    path('plan/<int:plan_id>', PlanIdView.as_view()),
]
