from django.db import models

class Agent(models.Model):
    class Meta:
        db_table = 'agents'

    id = models.BigAutoField(primary_key=True, db_comment='[PK]')
    name = models.CharField(max_length=50, db_comment="Агенты организации")
    conversation_goal = models.TextField()
    business_company = models.TextField()
    prompt = models.TextField()
    dialogue_analysis = models.TextField()
    tg_api_id = models.BigIntegerField(null=True, blank=True, db_comment='Telegram API ID агента')
    tg_api_hash = models.TextField(null=True, blank=True, db_comment='Telegram API hash агента')
    organizations = models.ManyToManyField('Organization', through='OrganizationAgent')

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}> Name:{self.name}"
