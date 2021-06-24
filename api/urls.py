from django.urls import path

from . import views

urlpatterns = [
    path('favorites/', views.favorites, name='favorites'),
]
