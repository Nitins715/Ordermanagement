from django import forms
from .models import NewOrder

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = NewOrder
        fields = '__all__'
        widgets = {
            'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'expected_collection_date': forms.DateInput(attrs={'type': 'date'}),
            'collection_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'fulfillment_date': forms.DateInput(attrs={'type': 'date'}),
            'sorted_date': forms.DateInput(attrs={'type': 'date'}),
        }
