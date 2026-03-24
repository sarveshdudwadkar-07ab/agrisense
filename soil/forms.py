from django import forms
from .models import SoilReport

class SoilReportForm(forms.ModelForm):
    class Meta:
        model = SoilReport
        fields = ['ph', 'nitrogen', 'phosphorus', 'potassium', 'organic_carbon']