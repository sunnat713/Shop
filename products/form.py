from django import forms
from products.models import ProductColorModel


class ColorModelForm(forms.ModelForm):
    class Meta:
        model = ProductColorModel
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }
