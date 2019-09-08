from rest_framework import serializers


class PageSerializer(serializers.Serializer):
    before = serializers.SerializerMethodField()
    after = serializers.SerializerMethodField()

    def get_before(self, obj):
        if obj.has_previous():
            return f"{self.context['request'].path}?page={obj.previous_page_number()}"

        return None

    def get_after(self, obj):
        if obj.has_next():
            return f"{self.context['request'].path}?page={obj.next_page_number()}"

        return None

    class Meta:
        fields = ('before', 'after')
