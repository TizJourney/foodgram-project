from django.urls import path

from . import views

urlpatterns = [
    path('favorites/', views.FavoritesView.as_view(), name='favorites'),
    path('favorites/<int:recipe_id>/', views.favorite_delete, name='favorites_delete'),
    path('subscriptions/', views.SubscriptionsView.as_view(), name='subscriptions'),
    path('subscriptions/<int:author_id>/', views.subscriptions_delete, name='subscriptions_delete'),
    path('ingredients/', views.ingredients, name='ingredients'),
]
