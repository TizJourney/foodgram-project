from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(required=False)
    class Meta:
        model = Recipe
        fields = (
            'name', 
            'breakfast_tag', 
            'lunch_tag', 
            'dinner_tag', 
            'ingredients',
            'time',
            'description',
            'image',
            )
        widgets = {
            'text': forms.Textarea(),
            'image': forms.FileInput(),
            'ingredients': forms.CheckboxSelectMultiple(),
        }
