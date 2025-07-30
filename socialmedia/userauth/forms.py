from django import forms
from .models import JobCircular

from django import forms
from .models import JobCircular

class JobCircularForm(forms.ModelForm):
    class Meta:
        model = JobCircular
        fields = ['title', 'company', 'location', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'required': True
            }),
        }
