from django.db import models
from superagent.models import SuperAgentModel


class UserModel(SuperAgentModel):
    phone = models.CharField(max_length=25)