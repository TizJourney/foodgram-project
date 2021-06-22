from django.shortcuts import render

from django.views.generic import CreateView

from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe




def index(request):
    return render(
        request,
        'recipes/recipes.html',
    )

class NewRecipe(CreateView):
    form_class = RecipeForm
    template_name = 'recipes/new.html'    

