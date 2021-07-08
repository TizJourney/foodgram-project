from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientQuanity, Purchases,
                     Recipe, RecipeTag, Subscriber)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
        'tags_list',
        'time',
        'description',
        'image',
        'favorite_count'
    )

    readonly_fields = ('favorite_count',)
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

    def favorite_count(self, obj):
        return obj.favorite_by_users.count()

    def tags_list(self, obj):
        return ', '.join([t.name for t in obj.tags.all()])


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'units',
    )
    search_fields = ('name',)
    list_filter = ('units',)


class IngredientQuanityAdmin(admin.ModelAdmin):
    pass


class SubscriberAdmin(admin.ModelAdmin):
    pass


class FavoriteAdmin(admin.ModelAdmin):
    pass


class PurchasesAdmin(admin.ModelAdmin):
    pass


class RecipeTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeTag, RecipeTagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientQuanity, IngredientQuanityAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchases, PurchasesAdmin)
