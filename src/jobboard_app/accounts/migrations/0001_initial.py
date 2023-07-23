# Generated by Django 4.2.2 on 2023-07-17 19:37

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(max_length=30)),
                ('house_number', models.PositiveSmallIntegerField()),
                ('office_number', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Adresses',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='City')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Gender')),
            ],
            options={
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name='profile',
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ('phone_number', models.CharField(max_length=20)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/avatar/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                (
                    'years_exp',
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(120)],
                        verbose_name='Years experience',
                    ),
                ),
                (
                    'city',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='profiles',
                        related_query_name='profile',
                        to='accounts.city',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
