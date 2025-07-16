from django import forms
from .models import JobCircular

class JobCircularForm(forms.ModelForm):
    class Meta:
        model = JobCircular
        fields = ['title', 'company', 'location', 'description']
