from django import forms
from .models import AgentModel
from superagent.forms import SuperAgentForm
from user.forms import UserForm

class AgentForm(forms.ModelForm):
    class Meta:
        model = AgentModel
        fields = '__all__'

class AgentCompositeForm(forms.Form):
    agent_form = AgentForm()
    superagent_form = SuperAgentForm()
    user_form = UserForm()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(self.agent_form.fields)
        self.fields.update(self.superagent_form.fields)
        self.fields.update(self.user_form.fields)

    def is_valid(self):
        return all([
            super().is_valid(),
            self.agent_form.is_valid(),
            self.superagent_form.is_valid(),
            self.user_form.is_valid()
        ])

    def save(self):
        agent_instance = self.agent_form.save()
        superagent_instance = self.superagent_form.save(commit=False)
        user_instance = self.user_form.save(commit=False)
        superagent_instance.agent = agent_instance
        user_instance.agent = agent_instance
        superagent_instance.save()
        user_instance.save()
