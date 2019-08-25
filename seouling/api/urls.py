from django.urls import path
from api.auth.auth_signin_email import SigninEmail
from api.auth.auth_signin_sns import SigninSNS
from api.auth.auth_signup import Signup
from api.auth.auth_token import CheckToken
from api.views import TMP

urlpatterns = [
    path('token', CheckToken.as_view()),
    path('signup', Signup.as_view()),
    path('signin/email', SigninEmail.as_view()),
    path('signin/sns', SigninSNS.as_view()),
    path('tmp', TMP.as_view()),
]
