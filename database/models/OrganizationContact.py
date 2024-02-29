from django.db import models

from .Contact import Contact
from .Organization import Organization

class OrganizationContact(models.Model):
    class Meta:
        db_table = 'organization__contact'

    contact = models.ForeignKey(Contact, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    organization = models.ForeignKey(Organization, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')

    def __str__(self):
        return f"{self.organization.__str__()} + {self.contact.__str__()}"
