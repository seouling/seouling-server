from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from utils.authentication import TokenAuthentication


schema_view = get_schema_view(
   openapi.Info(
      validators=['flex', 'ssv'],
      title="Seouling API",
      default_version='v1',
      description="서울 관광 도우미 서울링!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ABClass98@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   authentication_classes=(TokenAuthentication,),
   public=True,
   permission_classes=(AllowAny,),
)