from rest_framework import serializers
from api.models import Tag, TagItem


class TagItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagItem
        fields = ('id', 'content')


class TagSerializer(serializers.ModelSerializer):
    items = TagItemSerializer(many=True)

    class Meta:
        model = Tag
        fields = ('id', 'bundle_name', 'items')

