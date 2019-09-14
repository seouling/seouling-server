from django.urls import path, include

urlpatterns = [
    path('', include('api.plan.urls')),
    path('', include('api.auth.urls')),
    path('', include('api.schedule.urls')),
    path('', include('api.tag.urls')),
]
