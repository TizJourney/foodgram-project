from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, redirect, render

from .models import Recipe

from .forms import RecipeForm

RECIPE_PER_PAGE = 10

def _prepare_recipe_content(post_query, page_number):
    paginator = Paginator(post_query, RECIPE_PER_PAGE)
    page = paginator.get_page(page_number)
    return {'page': page, 'paginator': paginator}


def index(request):
    page_number = request.GET.get('page')
    recipe_query = (
        Recipe.objects
        .all()
    )

    context = _prepare_recipe_content(recipe_query, page_number)    

    return render(
        request,
        'recipes/recipes.html',
        context
    )

def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    isFavoried = request.user and recipe.favorite_by_users.filter(user=request.user).exists()

    context = {
        'recipe': recipe,
        'isFavoried': isFavoried,
    }
    return render(request, 'recipes/singlePage.html', context)


@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')

        return render(
            request,
            'recipes/new.html',
            {'form': form}
        )

    form = RecipeForm()
    return render(request, 'recipes/new.html', {'form': form})
