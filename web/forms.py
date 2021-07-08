from django import forms

from .models import Recipe, RecipeTag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=RecipeTag.objects.all(),
        to_field_name='slug'
    )
    ingredients = forms.CharField(required=False)

    class Meta:
        model = Recipe
        fields = (
            'name',
            'tags',
            'ingredients',
            'time',
            'description',
            'image',
        )
        widgets = {
            'text': forms.Textarea(),
            'image': forms.FileInput(),
        }
