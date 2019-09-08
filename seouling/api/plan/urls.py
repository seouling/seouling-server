from django.urls import path
from api.plan.plan import PlanView
from api.plan.plan_id import PlanIdView

urlpatterns = [
    path('', PlanView.as_view()),
    path('<int:plan_id>', PlanIdView.as_view()),
]
