from django.urls import path
from api.schedule.plan_id_schedule import PlanScheduleView
from api.schedule.schedule_id import ScheduleIdView

urlpatterns = [
    path('plan/<int:plan_id>/schedule', PlanScheduleView.as_view()),
    path('schedule/<int:schedule_id>', ScheduleIdView.as_view()),
]
