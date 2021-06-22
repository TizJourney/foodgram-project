from django.contrib import admin

from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'tags','time', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'



admin.site.register(Recipe, RecipeAdmin)
