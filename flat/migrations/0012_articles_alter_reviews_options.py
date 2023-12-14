# Generated by Django 4.1.7 on 2023-09-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0011_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/articles/%Y/%m/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=25000, verbose_name='Текст новости')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзывы', 'verbose_name_plural': 'Отзывы'},
        ),
    ]