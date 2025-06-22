# products/forms.py

from django import forms
from .models import BulkOrder

class BulkOrderForm(forms.ModelForm):
    class Meta:
        model = BulkOrder
        fields = ['full_name', 'phone', 'email', 'quantity', 'notes']
        labels = {
            'full_name': 'اسم التاجر أو الشركة',
            'phone': 'رقم الجوال',
            'email': 'البريد الإلكتروني',
            'quantity': 'الكمية المطلوبة (كجم)',
            'notes': 'ملاحظات إضافية',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
