import boto3
from api.models import User
import random
import string
from django.core.exceptions import ObjectDoesNotExist


# Todo: 이미지 업로드 구현
def upload_image_to_s3(image):
    pass


def create_token():
    letters = string.ascii_letters

    while True:
        token = ''.join(random.choice(letters) for _ in range(30))
        try:
            User.objects.get(token=token)
        except ObjectDoesNotExist:
            return token
