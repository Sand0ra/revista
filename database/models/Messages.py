from django.db import models

from .User import User
from .Dialogue import Dialogue

class Messages(models.Model):
    class Meta:
        db_table = 'messages'

    id = models.BigAutoField(primary_key=True, db_comment='[PK]')
    sender_type = models.TextField(blank=False)
    sender_user = models.ForeignKey(User, null=True, blank=True, db_comment='[FK]', on_delete=models.DO_NOTHING)
    dialogue_id = models.ForeignKey(Dialogue, blank=False, db_comment='[FK]', on_delete=models.DO_NOTHING)
    message = models.TextField(blank=False, default="")
    source = models.TextField(blank=False)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}>"