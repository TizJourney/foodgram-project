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

@decorators.api_view(['POST'])
def favorites(request):
    """
    фунциональность по изменению состояния любимых рецептов
    """

        # review = get_object_or_404(
        #     Review,
        #     id=self.kwargs.get('review_id'),
        #     title__id=self.kwargs.get('title_id')
        # )


    return response.Response('', status=status.HTTP_200_OK)


