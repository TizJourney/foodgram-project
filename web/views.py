from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm


def index(request):
    return render(
        request,
        'recipes/recipes.html',
    )


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
