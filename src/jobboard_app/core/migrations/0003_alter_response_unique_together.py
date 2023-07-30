# Generated by Django 4.2.2 on 2023-07-29 19:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_populate_tables_with_defaults'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('user', 'vacancy')},
        ),
    ]