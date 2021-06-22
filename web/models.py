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
    class Tags(models.TextChoices):
        BREAKFEAST = 'завтрак'
        DINNER = 'обед'
        SUPPER = 'ужин'

    TAGS_MAX_LENGTH = min(20, max((len(c[0]) for c in Tags.choices)))

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

    tags = models.CharField(
        max_length=TAGS_MAX_LENGTH,
        choices=Tags.choices,
        default=Tags.BREAKFEAST,
    )

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

    cook_time = models.IntegerField(
        'Время приготовления',
        validators=(
            MinValueValidator(0),
        )
    )

    image = models.ImageField(
        upload_to='recipes_images/',
        verbose_name='Изображение',
        help_text='Загрузка изображения. Опционально.'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        title = f'Рецепт {self.name}'
        return title


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик',
        help_text='Пользователь, который подписывается.',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Рецепт',
        help_text='Рецепт, на которого подписываются.',
    )

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        user = self.user
        recipe = self.recipe
        return f'Подписка @{user} на @{recipe}'
