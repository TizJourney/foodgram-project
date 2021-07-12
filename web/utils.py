from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Ingredient, IngredientQuanity, RecipeTag
from .serializers import (
    IngredientInputSerializer, IngredientQuanityInputSerializer
)

RECIPE_PER_PAGE = 6
FOLLOW_PER_PAGE = 6

NAME_PREFIX_LEN = len('nameIngredient_')
VALUE_PREFIX_LEN = len('valueIngredient_')
UNITS_PREFIX_LEN = len('unitsIngredient_')


def _create_uri(current_tag, filter_data):
    params = {
        tag.slug: not value if current_tag == tag else value
        for tag, value in filter_data.items()
    }
    return '&'.join(
        [f'{name}=0' for name, value in params.items() if not value]
    )


def _create_filter_context(request, recipe_tags):
    filter_query = Q(pk__in=[])
    filter_data = {}

    for tag in recipe_tags:
        filter_data[tag] = request.GET.get(tag.slug, '1') == '1'
        if filter_data[tag]:
            filter_query.add(Q(tags__slug=tag.slug), Q.OR)

    filter_context = {
        'default': _create_uri(None, filter_data),
        'filters': {}
    }
    for tag in recipe_tags:
        filter_context['filters'][tag] = {
            'uri': _create_uri(tag, filter_data),
            'value': filter_data[tag],
        }

    return filter_query, filter_context


def _prepare_recipe_content(post_query, request):
    """
    Общая функция по созданию контента для отрисовки карточек рецептов.
    Используется на основной странице, избранном, рецепте одного автора и т.п.
    """

    page_number = request.GET.get('page')

    user = request.user if request.user.is_authenticated else None

    filter_query, filter_context = _create_filter_context(
        request, list(RecipeTag.objects.all())
    )

    extended_query = post_query.filter(filter_query).distinct()

    if user is not None:
        favoriedQuery = Q(favorite_by_users__user=user)
        shopListQuery = Q(purchase_by_users__user=user)
        extended_query = (
            extended_query
            .annotate(is_favoried=Count(
                'favorite_by_users', filter=favoriedQuery)
            )
            .annotate(is_in_shop_list=Count(
                'purchase_by_users', filter=shopListQuery)
            )
        )

    paginator = Paginator(extended_query, RECIPE_PER_PAGE)
    page = paginator.get_page(page_number)
    return {
        'page': page,
        'paginator': paginator,
        'filter_context': filter_context,
    }


def _get_ingredients(request):
    """
    Функция для разбора набора инридиентов из формы,
    которая посылается в сайта
    Пример входного ключа: nameIngredient_1
    """
    ingridient_names = {}
    ingridient_values = {}
    ingridient_units = {}

    ingredients = []
    know_ingredients = set()

    if not request.POST:
        return []

    for key, value in request.POST.items():
        if key.startswith('nameIngredient'):
            ingridient_names[key[NAME_PREFIX_LEN:]] = value
        elif key.startswith('valueIngredient'):
            ingridient_values[key[VALUE_PREFIX_LEN:]] = value
        elif key.startswith('unitsIngredient'):
            ingridient_units[key[UNITS_PREFIX_LEN:]] = value

    for key, name in ingridient_names.items():
        new_item = {
                'name': name,
                'value': ingridient_values.get(key),
                'units': ingridient_units.get(key)
            }

        ingredient_serializer = IngredientInputSerializer(data={
            'name': new_item['name'],
            'units': new_item['units'],
        })
        if not ingredient_serializer.is_valid():
            error_message = (
                f'Неверное описание ингредиента "{name}"'
            )
            return None, error_message
        
        if not Ingredient.objects.filter(name=name).exists():
            error_message = (
                f'В базе данных нет ингредиента "{name}"'
            )
            return None, error_message

        quanity_serializer = IngredientQuanityInputSerializer(data={
            'value': new_item['value']
        })

        if not quanity_serializer.is_valid():
            error_message = (
                f'Неправильное количество ингредиента "{name}"'
            )
            return None, error_message

        if name in know_ingredients:
            error_message = (
                f'Невозможно создать рецепт с дубликатами ингредиента "{name}"'
            )
            return None, error_message

        ingredients.append(new_item)
        know_ingredients.add(name)
    return ingredients, None


def _save_recipe(form, author, ingredients, recipe=None):
    """
    Функция сохрания рецепта в базу данных
    Создаются дополнительно записи для ингредиентов
    """

    recipe_from_form = form.save(commit=False)
    if recipe is None:
        recipe_from_form.author = author
    recipe_from_form.save()

    recipe_from_form.ingredients_quantities.all().delete()

    for item in ingredients:
        ingredient = get_object_or_404(Ingredient, name=item['name'])
        recipe_ingredient = IngredientQuanity(
            recipe=form.instance,
            value=item['value'],
            ingredient=ingredient,
        )
        recipe_ingredient.full_clean()
        recipe_ingredient.save()
    form.save_m2m()


def _process_recipe_form(request, message, instance, nav_page, new):
    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance or None
    )

    if form.is_valid():
        ingredients, error = _get_ingredients(request)
        if error is not None:
            form.add_error(None, error)
        elif not ingredients:
            error = 'В форме должны быть ингредиенты'
        
        if error is None:
            _save_recipe(form, request.user, ingredients, instance)
            messages.add_message(request, messages.INFO, message)
            return redirect('index')

        # пересоздать формы не прошедшую валидацию
        form = RecipeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=instance or None
        )
        form.add_error(None, error)

    return render(
        request,
        'recipes/editRecipe.html',
        {'form': form, 'new': new, 'nav_page': nav_page}
    )
