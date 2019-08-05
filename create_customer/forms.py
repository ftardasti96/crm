from django import forms
from .models import PersonalData

class PersonalForm(forms.ModelForm):

    class Meta:
        model = PersonalData
        fields = '__all__'