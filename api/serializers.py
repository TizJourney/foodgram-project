from rest_framework import serializers

from web.models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'recipe',
            'user',
        )
        model = Favorite