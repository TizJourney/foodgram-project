from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):

    NAME_PREFIX_LEN = len('nameIngredient_')
    VALUE_PREFIX_LEN = len('valueIngredient_')
    UNITS_PREFIX_LEN  = len('unitsIngredient_')

    def __init__(self, data=None, *args, **kwargs):
        ingridient_names = {}
        ingridient_values = {}
        ingridient_units = {}

        self.ingridient_data = []

        if data is not None:
            for key, value in data.items():
                if key.startswith('nameIngredient'):
                    ingridient_names[key[self.NAME_PREFIX_LEN:]] = value
                elif key.startswith('valueIngredient'):
                    ingridient_values[key[self.VALUE_PREFIX_LEN:]] = value
                elif key.startswith('unitsIngredient'):
                    ingridient_units[key[self.UNITS_PREFIX_LEN:]] = value
            
            for key,value in ingridient_names.items():
                self.ingridient_data.append({
                    'name': value,
                    'value': ingridient_values.get(key),
                    'units': ingridient_units.get(key)
                })
        super().__init__(data, *args, **kwargs)            


    # метод-валидатор для поля subject
    def clean_ingredients(self):
        for item in self.ingridient_data:
            if None in item.values():
                raise forms.ValidationError(
                    "Неконсистентные данные формы ингридиентов"
                    )
        return self.ingridient_data

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
