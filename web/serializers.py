from rest_framework import serializers

from web.models import Ingredient, IngredientQuanity


class IngredientInputSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient


class IngredientQuanityInputSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('value', )
        model = IngredientQuanity
