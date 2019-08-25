from rest_framework.authentication import BaseAuthentication
from api.models import User
from rest_framework.authentication import get_authorization_header
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import exceptions
from django.utils.encoding import smart_text


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = get_authorization_header(request).split()
        if token is None:
            return None

        if len(token) <= 1:
            raise exceptions.AuthenticationFailed('인증 형식과 맞지 않습니다.')

        elif len(token) > 2:
            raise exceptions.AuthenticationFailed('인증 형식과 맞지 않습니다.')

        if settings.TOKEN_PREFIX.lower() != smart_text(token[0].lower()):
            return None

        try:
            user = User.objects.get(token=smart_text(token[1]))
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('유효하지 않은 토큰입니다.')

        request.user = user
        return (user, None)
