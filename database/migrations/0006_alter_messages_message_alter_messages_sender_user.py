# Generated by Django 5.0.1 on 2024-01-22 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_rename_sender_user_id_messages_sender_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender_user',
            field=models.ForeignKey(blank=True, db_comment='[FK]', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]