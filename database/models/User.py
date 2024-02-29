from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .CustomUserManager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'users'

    id = models.BigAutoField(primary_key=True, db_comment='[PK]')
    full_name = models.CharField(max_length=50, db_comment='Имя пользователя в админке')
    tg_id = models.BigIntegerField(null=True, blank=True, db_comment='Telegram ID')
    tg_nickname = models.TextField(null=True, blank=True, db_comment='Telegram nickname')
    email = models.TextField(unique=True, blank=False, db_comment='Email')
    organization = models.ForeignKey('Organization', null=True, blank=True, db_comment='[FK]', on_delete=models.DO_NOTHING)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ctime = models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}> Имя: {self.full_name}; Email: {self.email}"
