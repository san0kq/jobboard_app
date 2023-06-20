# Generated by Django 4.2.2 on 2023-06-19 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('street', models.CharField(max_length=30)),
                ('house_number', models.PositiveSmallIntegerField()),
                (
                    'office_number',
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    'city',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='adresses',
                        to='accounts.city',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=150, unique=True, verbose_name='Company name'
                    ),
                ),
                ('founded_in', models.PositiveSmallIntegerField()),
                (
                    'logo',
                    models.ImageField(blank=True, null=True, upload_to='image/logo/'),
                ),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('web_site', models.SlugField()),
                ('registred_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'adress',
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='core.adress',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=35)),
                (
                    'image',
                    models.ImageField(blank=True, null=True, upload_to='image/avatar/'),
                ),
                ('registred_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'city',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='employees',
                        to='accounts.city',
                    ),
                ),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='employees',
                        to='core.company',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Employees_number',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('size_range', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=20, unique=True, verbose_name='Rating'),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.CharField(max_length=800)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to='core.company',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'unique_together': {('user', 'company')},
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Vacancy name')),
                ('description', models.TextField()),
                ('registred_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='vacancies',
                        to='core.company',
                    ),
                ),
                (
                    'contracts',
                    models.ManyToManyField(
                        related_name='vacancies_contracts', to='accounts.contract'
                    ),
                ),
                (
                    'countries',
                    models.ManyToManyField(
                        related_name='vacancies_countries', to='accounts.country'
                    ),
                ),
                (
                    'employee',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='vacancies',
                        to='core.employee',
                    ),
                ),
                (
                    'levels',
                    models.ManyToManyField(
                        related_name='vacancies_levels', to='accounts.level'
                    ),
                ),
                (
                    'salary',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='vacancies',
                        to='accounts.salary',
                    ),
                ),
                (
                    'work_formats',
                    models.ManyToManyField(
                        related_name='vacancies_work_formats', to='accounts.workformat'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=30, unique=True, verbose_name='Tag'),
                ),
                (
                    'profile',
                    models.ManyToManyField(
                        related_name='profile_tags', to='accounts.profile'
                    ),
                ),
                (
                    'vacancies',
                    models.ManyToManyField(
                        related_name='vacancies_tags', to='core.vacancy'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('platform', models.CharField(max_length=100)),
                ('url', models.SlugField(unique=True)),
                (
                    'company',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='social_links',
                        to='core.company',
                    ),
                ),
                (
                    'profile',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='social_links',
                        to='accounts.profile',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=30, unique=True, verbose_name='Sector'),
                ),
                (
                    'companies',
                    models.ManyToManyField(
                        related_name='companies_sectors', to='core.company'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'status',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='responses',
                        to='accounts.status',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='responses',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'vacancy',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='responses',
                        to='core.vacancy',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=100, unique=True, verbose_name='Position'
                    ),
                ),
                (
                    'employees',
                    models.ManyToManyField(
                        related_name='employees_positions', to='core.employee'
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='employees_number',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='companies',
                to='core.employees_number',
            ),
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'rating',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to='core.rating',
                    ),
                ),
                (
                    'review',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='ratings',
                        to='core.review',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='ratings',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'unique_together': {('review', 'user')},
            },
        ),
    ]