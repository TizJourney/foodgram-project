from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):

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
        }
