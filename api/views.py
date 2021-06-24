from web.models import Favorite, Recipe, Subscriber
from django.shortcuts import render

from smtplib import SMTPException

from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (decorators, filters, mixins, permissions, response,
                            status, viewsets)
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required

from django.views import View
from rest_framework.decorators import api_view, renderer_classes
from django.http import JsonResponse
import json

from .serializers import FavoriteSerializer, SubscriberSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model

User = get_user_model()

@renderer_classes((JSONRenderer,))
class FavoritesView(View):
    """
    фунциональность по изменению состояния любимых рецептов
    """
    def get(self, request):
        return response.Response(request.user.favorite_recipes.all(), status=status.HTTP_200_OK)

    def post(self, request):
        json_data = json.loads(request.body)
        recipe = get_object_or_404(Recipe, pk=json_data.get('id'))
        obj, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse(FavoriteSerializer(obj).data, status=status.HTTP_200_OK)

@login_required
def favorite_delete(request, recipe_id):
    obj = get_object_or_404(Favorite, user=request.user, recipe__pk=recipe_id)
    obj.delete()
    return JsonResponse(FavoriteSerializer(obj).data, status=status.HTTP_200_OK)


@renderer_classes((JSONRenderer,))
class SubscriptionsView(View):
    """
    фунциональность по изменению состояния подписок на пользвотелей
    """
    def get(self, request):
        return response.Response(request.user.subscribing.all(), status=status.HTTP_200_OK)

    def post(self, request):
        json_data = json.loads(request.body)
        author = get_object_or_404(User, pk=json_data.get('id'))
        obj, created = Subscriber.objects.get_or_create(subscriber=request.user, author=author)
        return JsonResponse(SubscriberSerializer(obj).data, status=status.HTTP_200_OK)

@login_required
def subscriptions_delete(request, author_id):
    obj = get_object_or_404(Subscriber, subscriber=request.user, author__pk=author_id)
    obj.delete()
    return JsonResponse(SubscriberSerializer(obj).data, status=status.HTTP_200_OK)
