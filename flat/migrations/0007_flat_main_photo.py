# Generated by Django 4.1.7 on 2023-09-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0006_flat_main_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/flat/%Y/%m/', verbose_name='Главное фото'),
        ),
    ]
