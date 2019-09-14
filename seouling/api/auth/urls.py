from django.urls import path
from api.auth.auth_signin_email import SigninEmail
from api.auth.auth_signin_sns import SigninSNS
from api.auth.auth_signup import Signup
from api.auth.auth_token import CheckToken

urlpatterns = [
    path('auth/token', CheckToken.as_view()),
    path('auth/signup', Signup.as_view()),
    path('auth/signin/email', SigninEmail.as_view()),
    path('auth/signin/sns', SigninSNS.as_view())
]
