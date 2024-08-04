# Generated by Django 5.0.7 on 2024-07-30 15:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('access_token', models.CharField(max_length=50)),
                ('expires_in', models.DateTimeField()),
                ('refresh_token', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('oauth2_provider', models.CharField(default='notes', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('email', 'oauth2_provider')},
            },
        ),
    ]
