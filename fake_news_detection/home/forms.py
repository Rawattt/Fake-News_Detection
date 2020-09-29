from django import forms
from .models import Facts

class FactsForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = ['fact']