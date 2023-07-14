from django import forms
from .models import SuperAgentModel

class SuperAgentForm(forms.Form):
    class Meta:
        model = SuperAgentModel
        fields = '__all__'