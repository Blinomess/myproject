# Generated by Django 5.1.6 on 2025-04-16 18:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0011_remove_messages_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
