from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'name', 
            'tags', 
            'ingredients',
            'time',
            'description',
            'image'
            )
        widgets = {
            'text': forms.Textarea(),
            'image': forms.FileInput(),
        }
