# Generated by Django 4.1.7 on 2023-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0009_alter_flat_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='first_line',
            field=models.BooleanField(default=False, verbose_name='Первая линия'),
        ),
        migrations.AddField(
            model_name='flat',
            name='hot_offer',
            field=models.BooleanField(default=False, verbose_name='Горячее предложение'),
        ),
        migrations.AddField(
            model_name='flat',
            name='out_infra',
            field=models.BooleanField(default=False, verbose_name='Отельная инфраструктура'),
        ),
        migrations.AddField(
            model_name='flat',
            name='vip',
            field=models.BooleanField(default=False, verbose_name='Роскошная жизнь'),
        ),
    ]
