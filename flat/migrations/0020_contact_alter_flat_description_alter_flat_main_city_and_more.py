# Generated by Django 4.1.7 on 2023-10-14 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0019_alter_flat_main_type_real_estate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, max_length=10000, verbose_name='Сообщение')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Сообщение из формы',
                'verbose_name_plural': 'Сообщения из формы',
            },
        ),
        migrations.AlterField(
            model_name='flat',
            name='description',
            field=models.TextField(help_text='Обязательное поле', max_length=15000, verbose_name='Описание объекта'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='main_city',
            field=models.ForeignKey(help_text='Обязательное поле', on_delete=django.db.models.deletion.CASCADE, related_name='main_city', to='flat.city', verbose_name='Выберите город'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='main_country',
            field=models.ForeignKey(help_text='Обязательное поле', on_delete=django.db.models.deletion.CASCADE, related_name='main_country', to='flat.country', verbose_name='Выберите страну'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='main_offer',
            field=models.ForeignKey(help_text='Обязательное поле', on_delete=django.db.models.deletion.CASCADE, related_name='main_offer', to='flat.offer', verbose_name='Укажите от кого предложение'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='main_photo',
            field=models.ImageField(help_text='Обязательное поле', upload_to='media/flat/%Y/%m/', verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='main_type_real_estate',
            field=models.ForeignKey(help_text='Обязательное поле', on_delete=django.db.models.deletion.CASCADE, related_name='main_type_real_estate', to='flat.type_real_estate', verbose_name='Выберите тип недвижимости'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='title',
            field=models.CharField(help_text='Обязательное поле', max_length=255, verbose_name='Название объекта'),
        ),
    ]