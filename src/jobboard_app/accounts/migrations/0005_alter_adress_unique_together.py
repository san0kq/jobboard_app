# Generated by Django 4.2.2 on 2023-07-20 19:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adress',
            unique_together={('city', 'street', 'house_number', 'office_number')},
        ),
    ]
