from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'name', 
            'tags', 
            'ingredients',
            'cook_time',
            'description',
            'image'
            )
        widgets = {
            'text': forms.Textarea()
        }
