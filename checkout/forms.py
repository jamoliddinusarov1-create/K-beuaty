from django import forms
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ism Familiya'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+998 XX XXX XX XX'}),
            'address': forms.TextInput(attrs={'placeholder': 'Yetkazish manzili'}),
        }