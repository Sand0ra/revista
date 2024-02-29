from django.db import models

from .Customer import Customer
from .Organization import Organization

class CustomerOrganization(models.Model):
    class Meta:
        db_table = 'customer__organization'

    customer = models.ForeignKey(Customer, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    organization = models.ForeignKey(Organization, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')
    
    def __str__(self):
        return f"{self.customer.__str__()} + {self.organization.__str__()}"