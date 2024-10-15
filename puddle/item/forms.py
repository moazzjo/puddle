from django import forms

from .models import Item

INPUT_STYLE = 'w-full py-4 px-6 rounded-xl border'

class newItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_STYLE
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_STYLE
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_STYLE
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields = ('category', 'name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_STYLE
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_STYLE
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_STYLE
            })
        }
