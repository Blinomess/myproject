# Generated by Django 5.1.6 on 2025-04-16 18:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0009_remove_messages_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
