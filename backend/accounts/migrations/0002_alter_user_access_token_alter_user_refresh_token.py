# Generated by Django 5.0.7 on 2024-07-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access_token',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(max_length=255),
        ),
    ]