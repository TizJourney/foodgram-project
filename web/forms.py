from django import forms

from .models import Recipe, RecipeTag


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(required=False)
    tags= forms.ModelMultipleChoiceField(
        queryset=RecipeTag.objects.all(),
        to_field_name='slug'
    )

    class Meta:
        model = Recipe
        fields = (
            'name',
            'time',
            'description',
            'image',
        )
        widgets = {
            'text': forms.Textarea(),
            'image': forms.FileInput(),
            'ingredients': forms.CheckboxSelectMultiple(),
        }
