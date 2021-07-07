import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import generics, response, status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

from web.models import Favorite, Ingredient, Purchases, Recipe, Subscriber

from .serializers import (
    FavoriteSerializer, IngredientSerializer,
    PurchasesSerializer, SubscriberSerializer
)

User = get_user_model()


@renderer_classes((JSONRenderer,))
class FavoritesView(View):
    """
    фунциональность по изменению состояния любимых рецептов
    """

    def get(self, request):
        return response.Response(
            request.user.favorite_recipes.all(), status=status.HTTP_200_OK
        )

    def post(self, request):
        json_data = json.loads(request.body)
        recipe = get_object_or_404(Recipe, pk=json_data.get('id'))
        obj, _ = Favorite.objects.get_or_create(
            user=request.user, recipe=recipe)
        return JsonResponse(
            FavoriteSerializer(obj).data, status=status.HTTP_200_OK
        )


@login_required
def favorite_delete(request, recipe_id):
    """
    Удаление из избранного для пользователя
    """

    obj = get_object_or_404(Favorite, user=request.user, recipe__pk=recipe_id)
    obj.delete()
    return JsonResponse(
        FavoriteSerializer(obj).data, status=status.HTTP_200_OK
    )


@renderer_classes((JSONRenderer,))
class SubscriptionsView(View):
    """
    фунциональность по изменению состояния подписок на пользвотелей
    """

    def get(self, request):
        return response.Response(
            request.user.subscribing.all(), status=status.HTTP_200_OK
        )

    def post(self, request):
        json_data = json.loads(request.body)
        author = get_object_or_404(User, pk=json_data.get('id'))
        obj, _ = Subscriber.objects.get_or_create(
            subscriber=request.user, author=author)
        return JsonResponse(
            SubscriberSerializer(obj).data, status=status.HTTP_200_OK
        )


@login_required
def subscriptions_delete(request, author_id):
    """
    Удаление подписок пользователя
    """

    obj = get_object_or_404(
        Subscriber, subscriber=request.user, author__pk=author_id)
    obj.delete()
    return JsonResponse(
        SubscriberSerializer(obj).data, status=status.HTTP_200_OK
    )


@renderer_classes((JSONRenderer,))
class PurchasesView(View):
    """
    фунциональность по изменению состояния покупок пользователя
    """

    def get(self, request):
        return response.Response(
            request.user.recipe_purchases.all(), status=status.HTTP_200_OK
        )

    def post(self, request):
        json_data = json.loads(request.body)
        recipe = get_object_or_404(Recipe, pk=json_data.get('id'))
        obj, _ = Purchases.objects.get_or_create(
            user=request.user, recipe=recipe)
        return JsonResponse(
            PurchasesSerializer(obj).data, status=status.HTTP_200_OK
        )


@login_required
def purchases_delete(request, recipe_id):
    obj = get_object_or_404(
        Purchases, user=request.user, recipe__pk=recipe_id)
    obj.delete()
    return JsonResponse(
        PurchasesSerializer(obj).data, status=status.HTTP_200_OK
    )


class Ingredients(generics.ListAPIView):
    serializer_class = IngredientSerializer
    MAX_LIMIT = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if not query:
            return []
        
        return (
            Ingredient.objects
            .filter(name__istartswith=query.lower())[:self.MAX_LIMIT]
        )
