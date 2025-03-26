from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField()
    origin = forms.CharField()
    ingredients = forms.Textarea()
    description = forms.Textarea()
    image = forms.ClearableFileInput()
    category_id = forms.Select()
    preparation_time = forms.CharField()

    class Meta:
        model = Recipe
        fields = (
            "title",
            "origin",
            "category_id",
            "ingredients",
            "description",
            "preparation_time",
            "image",
        )
