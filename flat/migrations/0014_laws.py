# Generated by Django 4.1.7 on 2023-09-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0013_news_alter_articles_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/laws/%Y/%m/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=25000, verbose_name='Текст новости')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Закон',
                'verbose_name_plural': 'Законы',
            },
        ),
    ]
