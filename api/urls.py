from django.urls import path

from . import views

urlpatterns = [
    path('favorites/', views.FavoritesView.as_view(), name='favorites'),
    path('favorites/<int:recipe_id>/', views.favorite_delete, name='favorites_delete'),
]
