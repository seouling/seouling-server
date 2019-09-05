from django.urls import path, include

urlpatterns = [
    path('plan/', include('api.plan.urls')),
    path('auth/', include('api.auth.urls')),
]
