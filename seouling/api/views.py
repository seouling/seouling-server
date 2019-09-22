from rest_framework.views import APIView
from api.models import Spot, SpotTag, SpotPicture
from utils.category import kr_category
from utils.tag import kr_tag
from utils.gu import kr_gu
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import pandas as pd
import boto3
import io
import os


class Parsing(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY'),
                          aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY'))

        obj = s3.get_object(Bucket=os.getenv('AWS_S3_BUCKET_NAME'), Key="seouling-spots.xlsx")
        data = obj['Body'].read()
        df = pd.read_excel(io.BytesIO(data), encoding='utf-8')

        for index, row in df.iterrows():
            data = dict()
            data['category'] = kr_category.index(row['카테고리'])
            data['kr_name'] = row['장소명']
            data['en_name'] = row['영문 장소명']
            data['kr_content'] = row['한글설명']
            data['en_content'] = row['영문설명']
            data['kr_operation'] = row['운영시간 (Hours of Operation)']
            data['en_operation'] = row['Hours of Operation']
            data['recommend_time'] = row['추천 방문시간대 (Recommended time for visit)']
            data['kr_subway'] = row['지하철역 (Nearby Subway Station)']
            data['en_subway'] = row['Subway Station']
            data['line'] = row['노선']
            data['phone'] = row['전화번호 (Phone No.)']
            data['homepage'] = row['홈페이지 (Website)']
            data['kr_address'] = row['주소']
            data['en_address'] = row['영문주소']

            for index, gu in enumerate(kr_gu):
                if gu in data['kr_address']:
                    data['gu'] = index

            try:
                spot = Spot(**data)
                spot.save()
            except:
                continue

            image_url = f"https://seouling-storage.s3.ap-northeast-2.amazonaws.com/images/spot/{data['kr_name']}.jpg"
            spot_picture = SpotPicture(spot=spot, picture=image_url)
            spot_picture.save()

            tags = row['Tag'].split('/')
            for tag in tags:
                tag_index = kr_tag.index(tag)
                spot_tag = SpotTag(spot=spot, tag_id=tag_index)
                spot_tag.save()

        return Response(status=200, data={'message': 'success'})
