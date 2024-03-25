from .models import DataInfo
from django.forms import ModelForm, TextInput, DateTimeInput


class DataInfoForm(ModelForm):
    class Meta:
        model = DataInfo
        fields = ['number', 'date', 'price', 'product_name']

        widgets = {
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the receipt number'

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Enter the date'

            }),
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the product name'

            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the product price'

            })
        }