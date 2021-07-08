from django.urls import include, path

from . import views

"""
Это api для работы JavaScript'а сайта для интерактивных изменений сайта.
Смотри
web/static/api/Api.js 
чтобы найти код, который делает запросы сюда
"""

v1_url_patterns = [
    path(
        'favorites/',
        views.FavoritesView.as_view(),
        name='favorites'
    ),
    path(
        'favorites/<int:recipe_id>/',
        views.favorite_delete,
        name='favorites_delete'
    ),
    path(
        'subscriptions/',
        views.SubscriptionsView.as_view(), name='subscriptions'),
    path(
        'subscriptions/<int:author_id>/',
        views.subscriptions_delete,
        name='subscriptions_delete'
    ),
    path('purchases/', views.PurchasesView.as_view(), name='purchases'),
    path(
        'purchases/<int:recipe_id>/',
        views.purchases_delete, name='purchases_delete'),
    path('ingredients/', views.Ingredients.as_view(), name='ingredients'),
]

urlpatterns = [
    path('v1/', include(v1_url_patterns)),
]
