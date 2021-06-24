from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, null=True)
    measurement = models.CharField(
        'Единица измерения',
        max_length=200,
        help_text='Единица измерения ингридента. Обязательно к заполнению.'
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.TextField(
        'Название рецепта',
        help_text='Название рецепта. Обязательно к заполнению.'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
        help_text='Автор рецепта. Заполняется автоматически.',
        db_index=True
    )

    breakfast_tag = models.BooleanField('Завтрак', db_index=True)
    lunch_tag = models.BooleanField('Обед', db_index=True)
    dinner_tag = models.BooleanField('Ужин', db_index=True)

    ingredients = models.ManyToManyField(Ingredient, blank=True)

    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        help_text='Дата создания. По-умолчанию выставляется текущее время.',
        db_index=True
    )

    description = models.TextField(
        'Описание',
        max_length=2000,
        blank=True,
        null=True,
        help_text='Описание рецепта. Необязательно для заполнения',
    )

    time = models.IntegerField(
        'Время приготовления',
        validators=(
            MinValueValidator(0),
        )
    )

    image = models.ImageField(
        'Загрузить фото',
        upload_to='recipes/',
        help_text='Загрузка изображения. Опционально.',
        #todo: remove
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        title = f'Рецепт {self.name}'
        return title




class Subscriber(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Автор',
        help_text='Пользователь, на которого подписываются.',
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='Подписчик',
        help_text='Пользователь, который подписывается.',
    )

    class Meta:
        unique_together = ('author', 'subscriber')

    def __str__(self):
        user = self.user
        author = self.author
        return f'Подписка @{user} на @{author}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_recipes',
        verbose_name='Любимые рецепты',
        help_text='Любимые рецепты пользователя',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_by_users',
        verbose_name='Пользователи рецепта',
        help_text='Пользователи, подписанные на рецепт',
    )

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        user = self.user
        recipe = self.recipe
        return f'Запомнить для @{user} рецепт @{recipe}'