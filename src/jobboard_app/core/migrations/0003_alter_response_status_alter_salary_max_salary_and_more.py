# Generated by Django 4.2.2 on 2023-07-18 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_populate_tables_with_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='responses',
                related_query_name='response',
                to='core.status',
            ),
        ),
        migrations.AlterField(
            model_name='salary',
            name='max_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salary',
            name='min_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
