from django.db import models

class SuperAgentModel(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    
    class Meta:
        app_label = 'superagent'
        abstract = True
