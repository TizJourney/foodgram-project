from rest_framework import serializers

from web.models import Favorite, Subscriber


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'recipe',
            'user',
        )
        model = Favorite


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'author',
            'subscriber',
        )
        model = Subscriber
