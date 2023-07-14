from django.db import models
from superagent.models import SuperAgentModel

class AgentModel(SuperAgentModel):
    email = models.EmailField(max_length=30)