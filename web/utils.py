from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Ingredient, IngredientQuanity, RecipeTag

RECIPE_PER_PAGE = 6
FOLLOW_PER_PAGE = 6

NAME_PREFIX_LEN = len('nameIngredient_')
VALUE_PREFIX_LEN = len('valueIngredient_')
UNITS_PREFIX_LEN = len('unitsIngredient_')


def _prepare_recipe_content(post_query, request):
    """
    Общая функция по созданию контента для отрисовки карточек рецептов.
    Используется на основной странице, избранном, рецепте одного автора и т.п.
    """

    page_number = request.GET.get('page')

    user = request.user if request.user.is_authenticated else None

    filter_query = Q(pk__in=[])

    filter_context = {}
    for tag in RecipeTag.objects.all():
        filter_context[tag] = request.GET.get(tag.slug, '1')
        if filter_context[tag] == '1':
            filter_query.add(Q(tags__slug=tag.slug), Q.OR)

    extended_query = post_query.filter(filter_query)

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
        'filter': filter_context
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
        ingredients.append(
            {
                'name': name,
                'value': ingridient_values.get(key),
                'units': ingridient_units.get(key)
            }
        )
    return ingredients


def _save_recipe(form, author, ingredients, recipe=None):
    """
    Функция сохрания рецепта в базу данных
    Создаются дополнительно записи для ингридиентов
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
        recipe_ingredient.save()
    form.save_m2m()


def _process_recipe_form(request, message, instance, nav_page, new):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if instance is not None:
        form.instance = instance

    if form.is_valid():
        ingredients = _get_ingredients(request)
        if ingredients:
            _save_recipe(form, request.user, ingredients, instance)
            messages.add_message(request, messages.INFO, message)
            return redirect('index')
        form.add_error(None, 'В форме должны быть ингридиенты')

    return render(
        request,
        'recipes/editRecipe.html',
        {'form': form, 'new': new, 'nav_page': nav_page}
    )
