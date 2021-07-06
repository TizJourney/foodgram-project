"""
здесь находится фильтр для отрисовке в шапке приложения количества покупок
работает 1 раз на загрузке страницы, дальше изменения происходит через JS
"""


from django import template

register = template.Library()


@register.filter(is_safe=True)
def count_shop_items(user):
    return user.recipe_purchases.count()
