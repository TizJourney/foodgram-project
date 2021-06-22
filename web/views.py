from django.shortcuts import render


def index(request):
    return render(
        request,
        'recipes/recipes.html',
    )

def new_recipe(request):
    return render(
        request,
        'recipes/new.html',
    )    