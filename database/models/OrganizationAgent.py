from django.db import models

from .Agent import Agent
from .Organization import Organization

class OrganizationAgent(models.Model):

    class Meta:
        db_table = 'organization_agent'

    agent = models.ForeignKey(Agent, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    organization = models.ForeignKey(Organization, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')
    def __str__(self):
        return f"{self.agent.__str__()} + {self.organization.__str__()}"

