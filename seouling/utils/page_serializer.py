from rest_framework import serializers


class PageSerializer(serializers.Serializer):
    before = serializers.SerializerMethodField()
    after = serializers.SerializerMethodField()
    count = serializers.IntegerField()
    per_page = serializers.IntegerField()

    def get_before(self, obj):
        if obj.has_previous():
            return obj.previous_page_number()

        return None

    def get_after(self, obj):
        if obj.has_next():
            return obj.next_page_number()

        return None

    class Meta:
        fields = ('before', 'after' 'count', 'per_page')
