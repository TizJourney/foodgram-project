from django.urls import path

from . import views

urlpatterns = [
    path('favorites/', views.FavoritesView.as_view(), name='favorites'),
]
