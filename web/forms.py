from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(required=False)
    tags = forms.BooleanField()

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
            'tags': forms.CheckboxSelectMultiple(),
        }
