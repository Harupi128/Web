# Generated by Django 3.1.7 on 2022-01-27 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]
