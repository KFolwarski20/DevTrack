from django import forms
from .models import ProgrammingLog


class ProgrammingLogForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLog
        fields = ['language', 'hours']
        widgets = {
            'hours': forms.NumberInput(attrs={'step': 0.25, 'min': 0}),
        }
