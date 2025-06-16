from rest_framework import serializers
from .models import Feed, FeedItem

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class FeedItemSerializer(serializers.ModelSerializer):
    feed = FeedSerializer()

    class Meta:
        model = FeedItem
        fields = '__all__'

    def create(self, validated_data):
        feed_data = validated_data.pop('feed')
        feed, _ = Feed.objects.get_or_create(**feed_data)
        return FeedItem.objects.create(feed=feed, **validated_data)
