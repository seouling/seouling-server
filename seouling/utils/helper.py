from api.models import User
import random
import string
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta


def create_token():
    letters = string.ascii_letters

    while True:
        token = ''.join(random.choice(letters) for _ in range(30))
        try:
            User.objects.get(token=token)
        except ObjectDoesNotExist:
            return token


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
