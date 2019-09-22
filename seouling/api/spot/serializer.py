from rest_framework import serializers
from api.models import Spot, Comment
from api.auth.serializer import UserSimpleSerializer
from utils.gu import kr_gu, en_gu
from utils.category import kr_category, en_category
from utils.tag import kr_tag, en_tag


class SpotSerializer(serializers.ModelSerializer):
    gu = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    operation = serializers.SerializerMethodField()
    subway = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    visitor = serializers.IntegerField()
    like = serializers.IntegerField()

    def get_gu(self, obj):
        return kr_gu[obj.gu] if self.context['locale'] == "kr" else en_gu[obj.gu]

    def get_category(self, obj):
        return kr_category[obj.category] if self.context['locale'] == "kr" else en_category[obj.category]

    def get_name(self, obj):
        return obj.kr_name if self.context['locale'] == "kr" else obj.en_name

    def get_content(self, obj):
        return obj.kr_content if self.context['locale'] == "kr" else obj.en_content

    def get_operation(self, obj):
        return obj.kr_operation if self.context['locale'] == "kr" else obj.en_operation

    def get_subway(self, obj):
        return obj.kr_subway if self.context['locale'] == "kr" else obj.en_subway

    def get_address(self, obj):
        return obj.kr_address if self.context['locale'] == "kr" else obj.en_address

    def get_tags(self, obj):
        tags = obj.tags.all()
        return map(lambda tag: kr_tag[tag.tag_id] if self.context['locale'] == 'kr' else en_tag[tag.tag_id], tags)

    class Meta:
        model = Spot
        fields = ('id', 'gu', 'category', 'name', "content", "operation", "recommend_time",
                  'subway', "line", "phone", "homepage", "address", 'pictures', 'tags', 'like', 'visitor')


class SpotSimpleSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    subway = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.kr_name if self.context['locale'] == "kr" else obj.en_name

    def get_subway(self, obj):
        return obj.kr_subway if self.context['locale'] == "kr" else obj.en_subway

    def get_picture(self, obj):
        return obj.pictures.first()

    class Meta:
        model = Spot
        fields = ('id', 'name', 'subway', 'picture')


class SpotMySeoulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spot
        fields = ('id', 'name', 'gu', 'category')


class CommentSerializer(serializers.ModelSerializer):
    writer = UserSimpleSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'writer')
