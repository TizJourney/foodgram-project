from django import template

register = template.Library()


@register.filter(is_safe=True)
def count_shop_items(user):
    return user.recipe_purchases.count()
