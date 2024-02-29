from django.db import models

from .Agent import Agent
from .Customer import Customer
from .User import User

class Organization(models.Model):
    class Meta:
        db_table = 'organizations'

    id = models.AutoField(primary_key=True, db_comment='[PK]')
    title = models.CharField(max_length=20, db_comment='Название организации')
    tin = models.CharField(max_length=12, db_comment='ИНН', default='', unique=True)
    owner = models.ForeignKey(User, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING, related_name='+')
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')
    agents = models.ManyToManyField(Agent, through='OrganizationAgent')
    customers = models.ManyToManyField(Customer, through='CustomerOrganization')
    contacts = models.ManyToManyField('Contact', through='OrganizationContact', related_name='organizations_contacts')

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}> Название: {self.title}"
