# Generated by Django 3.0 on 2020-10-12 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('no_induk', models.CharField(blank=True, max_length=10, verbose_name='Nomor Induk')),
                ('faculty', models.CharField(blank=True, max_length=128, verbose_name='fakultas')),
                ('role', models.CharField(max_length=100)),
                ('study_program', models.CharField(blank=True, max_length=128, verbose_name='program studi')),
                ('educational_program', models.CharField(blank=True, max_length=128, verbose_name='program pendidikan')),
                ('no_hp', models.CharField(blank=True, max_length=50, null=True)),
                ('foto_profil', models.CharField(blank=True, max_length=5000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profile',
            },
        ),
    ]
