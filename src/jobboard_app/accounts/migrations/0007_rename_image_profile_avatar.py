# Generated by Django 4.2.2 on 2023-07-23 21:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0006_alter_adress_office_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
    ]
