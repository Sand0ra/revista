# Generated by Django 5.0.1 on 2024-01-15 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(db_comment='[PK]', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_comment='Имя пользователя в админке', max_length=50)),
                ('tg_id', models.BigIntegerField(db_comment='Telegram ID', unique=True)),
                ('tg_nickname', models.TextField(db_comment='Telegram nickname', unique=True)),
                ('email', models.TextField(db_comment='Email', unique=True)),
                ('password', models.CharField(db_comment='Пароль админки', max_length=32)),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(db_comment='[PK]', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_comment='Имя пользователя в админке', max_length=50)),
                ('tg_id', models.BigIntegerField(db_comment='Telegram ID')),
                ('tg_nickname', models.TextField(db_comment='Telegram nickname')),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
            ],
            options={
                'db_table': 'customers',
                'unique_together': {('full_name', 'tg_id', 'tg_nickname')},
            },
        ),
        migrations.CreateModel(
            name='CustomerOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
                ('customer', models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.customer')),
            ],
            options={
                'db_table': 'customer__organization',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(db_comment='[PK]', primary_key=True, serialize=False)),
                ('title', models.CharField(db_comment='Название организации', max_length=20)),
                ('tg_api_id', models.BigIntegerField(db_comment='Telegram API ID аккаунта для рассылки', unique=True)),
                ('tg_api_hash', models.TextField(db_comment='Telegram API hash аккаунта для рассылки')),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
                ('customers', models.ManyToManyField(through='database.CustomerOrganization', to='database.customer')),
                ('owner', models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.user')),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(db_comment='[PK]', primary_key=True, serialize=False)),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
                ('customer', models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.customer')),
                ('organization', models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.organization')),
            ],
            options={
                'db_table': 'dialogues',
            },
        ),
        migrations.AddField(
            model_name='customerorganization',
            name='organization',
            field=models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.organization'),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(db_comment='[PK]', primary_key=True, serialize=False)),
                ('sender_type', models.TextField()),
                ('message', models.TextField(default="''::text")),
                ('source', models.TextField()),
                ('ctime', models.DateTimeField(auto_now_add=True, db_comment='Дата и время создания записи')),
                ('dialogue_id', models.ForeignKey(db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.dialogue')),
                ('sender_user_id', models.ForeignKey(blank=True, db_comment='[FK]', on_delete=django.db.models.deletion.DO_NOTHING, to='database.user')),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
