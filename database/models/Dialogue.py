from django.db import models

from .Organization import Organization
from .Customer import Customer

class Dialogue(models.Model):
    class Meta:
        db_table = 'dialogues'

    id = models.AutoField(primary_key=True, db_comment='[PK]')
    organization = models.ForeignKey(Organization, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')

    def __str__(self):
        return (
            f"<{self.__class__.__name__}: {self.id}> "
            f"Организация: {self.organization.__str__()} + "
            f"Покупатель: {self.customer.__str__()}"
        )

