from django.db import models

class Contact(models.Model):
    class Meta:
        db_table = 'contact'

    id = models.BigAutoField(primary_key=True, db_comment='[PK]')
    first_name = models.CharField(max_length=50, db_comment='Имя')
    last_name = models.CharField(max_length=50, db_comment='Фамилия')
    tg_nickname = models.CharField(max_length=50, null=True, blank=True, db_comment='Telegram nickname')
    organization = models.ManyToManyField('Organization', through='OrganizationContact', related_name='Org_contacts')
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')

    def __str__(self):
        return f"{self.organization.__str__()} + {self.contact.__str__()}"