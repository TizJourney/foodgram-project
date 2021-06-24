from web.models import Favorite, Recipe
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

from .serializers import FavoriteSerializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
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
        return JsonResponse(FavoriteSerializer(obj), status=status.HTTP_200_OK)


