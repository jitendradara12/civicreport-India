from django import forms
from .models import InfrastructureReport

class ReportForm(forms.ModelForm):
    class Meta:
        model = InfrastructureReport
        fields = ['category', 'severity', 'description', 'location']