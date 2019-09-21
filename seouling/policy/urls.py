from django.urls import path
from policy.views import privacy_policy

urlpatterns = [
    path('privacy_policy', privacy_policy),
]