from collections import defaultdict

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Purchases, Recipe

from .utils import _prepare_recipe_content, _process_recipe_form

FOLLOW_PER_PAGE = 6

User = get_user_model()


def index(request):
    """
    Основная страница рецептов. Доступна всем пользователям.
    """
    recipe_query = (
        Recipe.objects
        .all()
    )

    context = _prepare_recipe_content(
        recipe_query,
        request
    )
    context['title'] = 'Рецепты'
    context['nav_page'] = 'index'

    return render(
        request,
        'recipes/recipes.html',
        context
    )


def recipes_by_author(request, author_id):
    """
    Отрисовка списка рецептов конкртного автора
    """

    author = get_object_or_404(User, id=author_id)

    recipe_query = (
        Recipe.objects.filter(author=author)
        .all()
    )

    context = _prepare_recipe_content(
        recipe_query,
        request
    )
    context['title'] = f'{author}'
    context['nav_page'] = 'author'

    return render(
        request,
        'recipes/recipes.html',
        context
    )


@login_required
def favorite(request):
    """
    Отрисовка списка любимых рецептов
    """

    recipe_query = (
        Recipe
        .objects
        .filter(favorite_by_users__user=request.user)

    )

    context = _prepare_recipe_content(
        recipe_query,
        request
    )

    context['title'] = 'Избранное'
    context['nav_page'] = 'favorite'

    return render(
        request,
        'recipes/recipes.html',
        context
    )


def recipe_view(request, recipe_id):
    """
    Отрисовка детальной информации о одном рецепте
    """

    recipe = get_object_or_404(Recipe, id=recipe_id)
    is_favoried = (
        request.user.is_authenticated
        and recipe.favorite_by_users.filter(user=request.user).exists()
    )
    is_subscribed = (
        request.user.is_authenticated
        and recipe.author.subscribed_by_user.filter(
            subscriber=request.user).exists()
    )
    is_in_shop_list = (
        request.user.is_authenticated
        and recipe.purchase_by_users.filter(user=request.user).exists()
    )

    context = {
        'recipe': recipe,
        'is_favoried': is_favoried,
        'is_subscribed': is_subscribed,
        'is_in_shop_list': is_in_shop_list,
        'nav_page': 'single',
    }
    return render(request, 'recipes/singlePage.html', context)


@login_required
def edit_recipe(request, recipe_id):
    """
    Функциональность редактирования существующего рецепта
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not request.user.is_superuser and request.user != recipe.author:
        raise PermissionDenied()

    return _process_recipe_form(
        request,
        message='Рецепт успешно изменён',
        instance=recipe,
        nav_page='edit_recipe',
        new=False
    )


@login_required
def new_recipe(request):
    """
    Функциональность создания нового рецепта
    """
    return _process_recipe_form(
        request,
        message='Рецепт успешно создан',
        instance=None,
        nav_page='new_recipe',
        new=True
    )


@login_required
def follow_view(request):
    """
    Отрисовка страницы подписок на других пользователей
    для текущего пользователя
    """

    page_number = request.GET.get('page')

    follow_query = (
        request.user.subscribed_to_user
        .filter(subscriber=request.user)
        .prefetch_related('author__recipes')
    )

    paginator = Paginator(follow_query, FOLLOW_PER_PAGE)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
        'nav_page': 'follow',
    }

    return render(
        request,
        'recipes/follow.html',
        context
    )


@login_required
def delete_recipe(request, recipe_id):
    """
    Удаление рецепта пользователя
    """

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not request.user.is_superuser and request.user != recipe.author:
        raise PermissionDenied()
    recipe.delete()
    messages.add_message(request, messages.INFO, 'Рецепт успешно удалён')
    return redirect('index')
    


@login_required
def shop_list(request):
    """
    Отрисовка списка покупок пользователя
    """

    query = Recipe.objects.filter(purchase_by_users__user=request.user)

    context = {
        'shop_list': query,
        'nav_page': 'shop_list',
    }

    return render(
        request,
        'recipes/shopList.html',
        context
    )


@login_required
def shop_list_delete(request, recipe_id):
    """
    Удаление элемента из списка покупок
    """

    obj = get_object_or_404(
        Purchases, user=request.user, recipe__pk=recipe_id)
    obj.delete()
    return redirect('shop_list')


@login_required
def shop_list_download(request):
    """
    Функциональность создания и посылки пользователю файла со списком покупок
    """
    query_list = list(
        Recipe.objects
        .filter(purchase_by_users__user=request.user)
        .prefetch_related('ingredients')
    )
    shop_list_data = defaultdict(int)
    for item in query_list:
        for ing in item.ingredients_quantities.all():
            shop_list_data[ing.ingredient] += ing.value
    content = '\n'.join(
        [
            f'* {ing.name} ({ing.units}) - {value} '
            for ing, value in shop_list_data.items()
        ]
    )

    response = HttpResponse(content, content_type='text/plain; charset=utf8')
    response['Content-Disposition'] = 'attachment; filename=shop_list.txt'
    return response


