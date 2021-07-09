from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(
        'Единица измерения',
        max_length=200,
        help_text='Единица измерения ингридента. Обязательно к заполнению.'
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class RecipeTag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    color = models.SlugField(max_length=40,)

    class Meta:
        verbose_name = 'Тег рецепта'
        verbose_name_plural = 'Теги рецепта'

    def __str__(self):
        title = f'Тег рецепта "{self.name}"'
        return title


class Recipe(models.Model):
    name = models.TextField(
        'Название рецепта',
        help_text='Название рецепта. Обязательно к заполнению.'
    )

    tags = models.ManyToManyField(
        RecipeTag,
        verbose_name="Теги",
        blank=True,
        db_index=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
        help_text='Автор рецепта. Заполняется автоматически.',
        db_index=True
    )

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

    time = models.PositiveIntegerField(
        'Время приготовления',
        validators=(
            MinValueValidator(
                1, message='Время приготовления не меньше 1 минуты'
            ),
        )
    )

    image = models.ImageField(
        'Загрузить фото',
        upload_to='recipes/',
        help_text='Загрузка изображения. Опционально.',
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


class IngredientQuanity(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_quantities',
        verbose_name='ингридент',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients_quantities',
        verbose_name='рецепт',
    )
    value = models.PositiveIntegerField(
        'Количество единиц в рецепте',
        validators=(
            MinValueValidator(
                1, message='Количество не может быть меньше 1'
            ),
        )
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique__ingredient_quanity__recipe_ingredient'
            )
        ]
        verbose_name = 'Количество ингридиента'
        verbose_name_plural = 'Количества ингридиентов'

    def __str__(self):
        name = self.ingredient.name
        recipe = self.recipe.name
        value = self.value
        return (
            f'В рецепте "{recipe}" '
            f'используется "{name}" в количестве {value}'
        )


class Subscriber(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribed_by_user',
        verbose_name='Автор',
        help_text='Пользователь, на которого подписываются.',
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribed_to_user',
        verbose_name='Подписчик',
        help_text='Пользователь, который подписывается.',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'subscriber'],
                name='unique__subscriber__author_subscriber'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        subscriber = self.subscriber
        author = self.author
        return f'Подписка @{subscriber} на @{author}'


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
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique__favorite__user_recipe'
            )
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        user = self.user
        recipe = self.recipe
        return f'Запомнить для @{user} рецепт @{recipe}'


class Purchases(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_purchases',
        verbose_name='Список покупок',
        help_text='Список покупок пользователя',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='purchase_by_users',
        verbose_name='В покупках у пользвателя',
        help_text='Пользователи, у которых рецепт в покупках',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique__purchases__user_recipe'
            )
        ]
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        user = self.user
        recipe = self.recipe
        return f'Покупка для @{user} рецепта @{recipe}'
