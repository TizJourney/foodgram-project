from django.conf.urls import handler404, handler500  # noqa
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:author_id>/', views.recipes_by_author, name='recipes_by_author'),
    path('favorite', views.favorite, name='favorite'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_view, name='recipe'),
    path('follow/', views.follow_view, name='follow'),
    # path('follow/', views.follow_index, name='follow_index'),
#     path('group/<slug:slug>/', views.group_posts, name='group'),

#     path('<str:username>/', views.profile, name='profile'),
#     path('<str:username>/<int:post_id>/', views.post_view, name='post'),
#     path(
#         '<str:username>/<int:post_id>/edit/',
#         views.post_edit, name='post_edit'
#     ),
#     path(
#         '<username>/<int:post_id>/comment/',
#         views.add_comment,
#         name='add_comment'
#     ),
#     path(
#         '<str:username>/follow/',
#         views.profile_follow,
#         name="profile_follow"
#     ),
#     path(
#         '<str:username>/unfollow/',
#         views.profile_unfollow,
#         name="profile_unfollow"
#     ),
]
