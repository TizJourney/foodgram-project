from rest_framework import serializers

from web.models import Favorite, Ingredient, Purchases, Subscriber


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


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient


class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Purchases
