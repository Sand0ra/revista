from django.db import models

from database.validators import validate_tg_nickname

class Customer(models.Model):

    class Meta:
        db_table = 'customers'
        unique_together = ('full_name', 'tg_id', 'tg_nickname')

    id = models.BigAutoField(primary_key=True, db_comment='[PK]')
    full_name = models.CharField(max_length=50, db_comment='Имя пользователя в админке')
    tg_id = models.BigIntegerField(null=True, blank=True, db_comment='Telegram ID')
    tg_nickname = models.TextField(null=True, blank=True,
                                   validators=[validate_tg_nickname,],
                                   db_comment='Telegram nickname',
                                   )
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')
    organizations = models.ManyToManyField('Organization', through='CustomerOrganization')

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}> TG nickname: {self.tg_nickname}"
