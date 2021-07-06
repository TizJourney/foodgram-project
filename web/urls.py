from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:author_id>/', views.recipes_by_author, name='recipes_by_author'),
    path('favorite', views.favorite, name='favorite'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_view, name='recipe'),
    path('recipe_delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),    
    path('follow/', views.follow_view, name='follow'),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('shop_list_delete/<int:recipe_id>/', views.shop_list_delete, name='shop_list_delete'),
    path('shop_list_download/', views.shop_list_download, name='shop_list_download'),
]
