from django.contrib import admin

from django.contrib import admin

from .models import Recipe, Ingredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
        'breakfast_tag',
        'dinner_tag',
        'lunch_tag',
        'time',
        'description',
        'image'
    )
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'dimension',
    )
    search_fields = ('title',)
    list_filter = ('dimension',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
