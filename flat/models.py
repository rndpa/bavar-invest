from django.db import models
from django.urls import reverse
from PIL import Image
from flat.models import *
from modeltranslation.admin import TranslationAdmin

# Страна


class Country(models.Model):
    country = models.CharField(
        'Страна', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


# Город
class City(models.Model):
    city = models.CharField('Город', max_length=255,
                            blank=True, null=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


# Район
class District(models.Model):
    district = models.CharField('Район', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


# Тип недвижимости
class Type_real_estate(models.Model):
    type_real_estate = models.CharField(
        'Тип недвижимости', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.type_real_estate

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'


# комнаты
class Rooms(models.Model):
    rooms = models.CharField('Количество комнат', max_length=255)

    def __str__(self):
        return self.rooms

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


# Предложение
class Offer(models.Model):
    offer = models.CharField('От кого предложение', max_length=255)

    def __str__(self):
        return self.offer

    class Meta:
        verbose_name = 'От кого пердложение'
        verbose_name_plural = 'От кого предложение'


# Статус
class Status(models.Model):
    title = models.CharField('Статус', max_length=255)

    def __str__(self):
        return self.title()

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


# Инфраструктура
class Infrastructure(models.Model):
    title = models.CharField('Инфраструктура', max_length=255)

    def __str__(self):
        return self.title()

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'


# Основной класс недвижимости
class Flat(models.Model):
    title = models.CharField(
        'Название объекта', max_length=255, blank=False, unique=False, null=False, help_text='Обязательное поле')

    price = models.IntegerField(
        'Цена объекта', blank=True, null=True, help_text='EURO')

    square = models.FloatField(
        'Площадь объекта', blank=True, null=True, help_text='m2')

    year_of_construction = models.SmallIntegerField(
        'Год постройки', blank=True, null=True, help_text='Пример 2023')

    furniture = models.BooleanField(
        'Если есть мебель - отметье', blank=True, null=True)

    to_sea = models.FloatField(
        'Расстояние до моря в киллометрах', blank=True, null=True, help_text='Пример (0.2)')
    to_center = models.FloatField(
        'Расстояние до центра в киллометрах', blank=True, null=True, help_text='Пример (2.2)')
    to_airport = models.FloatField(
        'Расстояние до аэропорта в киллометрах', blank=True, null=True, help_text='Пример (8.9)')

    description = models.TextField(
        'Описание объекта', max_length=15000, blank=False, null=False, help_text='Обязательное поле')

    main_country = models.ForeignKey(
        Country, blank=False, null=False, related_name='main_country', on_delete=models.CASCADE, verbose_name='Выберите страну', help_text='Обязательное поле')
    main_city = models.ForeignKey(
        City, blank=False, null=False, related_name='main_city', on_delete=models.CASCADE, verbose_name='Выберите город', help_text='Обязательное поле')
    main_type_real_estate = models.ForeignKey(
        Type_real_estate, blank=False, null=False, related_name='main_type_real_estate', on_delete=models.CASCADE, verbose_name='Выберите тип недвижимости', help_text='Обязательное поле')
    main_rooms = models.ForeignKey(
        Rooms, blank=True, null=True, related_name='main_rooms', on_delete=models.CASCADE, verbose_name='Выберите комнаты')
    main_offer = models.ForeignKey(
        Offer, blank=False, null=False, related_name='main_offer', on_delete=models.CASCADE, verbose_name='Укажите от кого предложение', help_text='Обязательное поле')
    main_district = models.ForeignKey(District, blank=True, null=True,
                                      related_name='main_district', on_delete=models.CASCADE, verbose_name='Район')
    main_status = models.ForeignKey(
        Status, blank=True, null=True, related_name='main_status', on_delete=models.CASCADE, verbose_name='Статус')
    main_infrastructure = models.ForeignKey(
        Infrastructure, blank=True, null=True, related_name='main_infrastructure', on_delete=models.CASCADE, verbose_name='Инфраструктура')

    hot_offer = models.BooleanField('Горячее предложение', default=False)
    first_line = models.BooleanField('Первая линия', default=False)
    out_infra = models.BooleanField('Отельная инфраструктура', default=False)
    vip = models.BooleanField('Роскошная жизнь', default=False)

    wireless_Internet = models.BooleanField(
        'Беспроводной интернет', default=True)
    billiard = models.BooleanField('Бильярд', default=True)
    electric_generator = models.BooleanField('Электрогенератор', default=True)
    Green_Garden = models.BooleanField('Зеленый сад', default=True)
    finnish_sauna = models.BooleanField('Финская сауна', default=True)
    jacuzzi = models.BooleanField('Джакузи', default=True)
    playground = models.BooleanField('Детская площадка', default=True)
    video_surveillance = models.BooleanField('Видеонаблюдение', default=True)
    table_tennis = models.BooleanField('Настольный теннис', default=True)
    indoor_swimming_pool = models.BooleanField(
        'Закрытый бассейн', default=True)
    roman_Steam_Room = models.BooleanField('Римская парная', default=True)
    satellite_TV = models.BooleanField('Спутниковое ТВ', default=True)
    massage_rooms = models.BooleanField('Массажные кабинеты', default=True)
    fitness_center = models.BooleanField('Фитнес центр', default=True)
    turkish_hamam = models.BooleanField('Турецкий хамам', default=True)
    play_room = models.BooleanField('Игровая комната', default=True)
    children_pool = models.BooleanField('Детский бассейн', default=True)
    outdoor_swimming_pool = models.BooleanField(
        'Открытый бассейн', default=True)
    gazebos_for_recreation = models.BooleanField(
        'Беседки для отдыха', default=True)
    covered_parking = models.BooleanField('Крытая парковка', default=True)
    outdoor_parking = models.BooleanField('Открытая парковка', default=True)

    main_photo = models.ImageField(
        'Главное фото', upload_to='media/flat/%Y/%m/', blank=False, null=False, help_text='Обязательное поле')

    photo1 = models.ImageField(
        'Фото 1', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo2 = models.ImageField(
        'Фото 2', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo3 = models.ImageField(
        'Фото 3', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo4 = models.ImageField(
        'Фото 4', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo5 = models.ImageField(
        'Фото 5', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo6 = models.ImageField(
        'Фото 6', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo7 = models.ImageField(
        'Фото 7', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo8 = models.ImageField(
        'Фото 8', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo9 = models.ImageField(
        'Фото 9', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo10 = models.ImageField(
        'Фото 10', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo11 = models.ImageField(
        'Фото 11', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo12 = models.ImageField(
        'Фото 12', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo13 = models.ImageField(
        'Фото 13', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo14 = models.ImageField(
        'Фото 14', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo15 = models.ImageField(
        'Фото 15', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo16 = models.ImageField(
        'Фото 16', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo17 = models.ImageField(
        'Фото 17', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo18 = models.ImageField(
        'Фото 18', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo19 = models.ImageField(
        'Фото 19', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo20 = models.ImageField(
        'Фото 20', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo21 = models.ImageField(
        'Фото 21', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo22 = models.ImageField(
        'Фото 22', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo23 = models.ImageField(
        'Фото 23', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo24 = models.ImageField(
        'Фото 24', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo25 = models.ImageField(
        'Фото 25', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo26 = models.ImageField(
        'Фото 26', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo27 = models.ImageField(
        'Фото 27', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo28 = models.ImageField(
        'Фото 28', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo29 = models.ImageField(
        'Фото 29', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo30 = models.ImageField(
        'Фото 30', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo31 = models.ImageField(
        'Фото 31', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo32 = models.ImageField(
        'Фото 32', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo33 = models.ImageField(
        'Фото 33', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo34 = models.ImageField(
        'Фото 34', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)
    photo35 = models.ImageField(
        'Фото 35', upload_to='media/flat/add_photo/%Y/%m/', blank=True, null=True)

    slug = models.SlugField('URL', max_length=255, unique=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save()

        if self.main_photo:
            img = Image.open(self.main_photo.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.main_photo.path)

        if self.photo1:
            img = Image.open(self.photo1.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo1.path)

        if self.photo2:
            img = Image.open(self.photo2.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo2.path)

        if self.photo3:
            img = Image.open(self.photo3.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo3.path)

        if self.photo4:
            img = Image.open(self.photo4.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo4.path)

        if self.photo5:
            img = Image.open(self.photo5.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo5.path)

        if self.photo6:
            img = Image.open(self.photo6.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo6.path)

        if self.photo7:
            img = Image.open(self.photo7.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo7.path)

        if self.photo8:
            img = Image.open(self.photo8.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo8.path)

        if self.photo9:
            img = Image.open(self.photo9.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo9.path)

        if self.photo10:
            img = Image.open(self.photo10.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo10.path)

        if self.photo11:
            img = Image.open(self.photo11.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo11.path)

        if self.photo12:
            img = Image.open(self.photo12.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo12.path)

        if self.photo13:
            img = Image.open(self.photo13.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo13.path)

        if self.photo14:
            img = Image.open(self.photo14.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo14.path)

        if self.photo15:
            img = Image.open(self.photo15.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo15.path)

        if self.photo16:
            img = Image.open(self.photo16.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo16.path)

        if self.photo17:
            img = Image.open(self.photo17.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo17.path)

        if self.photo18:
            img = Image.open(self.photo18.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo18.path)

        if self.photo19:
            img = Image.open(self.photo19.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo19.path)

        if self.photo20:
            img = Image.open(self.photo20.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo20.path)

        if self.photo21:
            img = Image.open(self.photo21.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo21.path)

        if self.photo22:
            img = Image.open(self.photo22.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo22.path)

        if self.photo23:
            img = Image.open(self.photo23.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo23.path)

        if self.photo24:
            img = Image.open(self.photo24.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo24.path)

        if self.photo25:
            img = Image.open(self.photo25.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo25.path)

        if self.photo26:
            img = Image.open(self.photo26.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo26.path)

        if self.photo27:
            img = Image.open(self.photo27.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo27.path)

        if self.photo28:
            img = Image.open(self.photo28.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo28.path)

        if self.photo29:
            img = Image.open(self.photo29.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo29.path)

        if self.photo30:
            img = Image.open(self.photo30.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo30.path)

        if self.photo31:
            img = Image.open(self.photo31.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo31.path)

        if self.photo32:
            img = Image.open(self.photo32.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo32.path)

        if self.photo33:
            img = Image.open(self.photo33.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo33.path)

        if self.photo34:
            img = Image.open(self.photo34.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo34.path)

        if self.photo35:
            img = Image.open(self.photo35.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.photo35.path)

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = ' Объект недвижимости'
        verbose_name_plural = ' Объекты недвижимости'


class Reviews(models.Model):
    name = models.CharField('Имя', max_length=255, blank=False, null=False)
    text = models.TextField(
        'Текст отзыва', max_length=15000, blank=False, null=False)
    data = models.CharField('Дата', max_length=100, blank=False,
                            null=False, help_text='Введите дату в формате 01.01.2021')
    photo = models.ImageField(
        'Фото', blank=True, null=False, upload_to='media/reviews/%Y/%m/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("reviews_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class Articles(models.Model):
    photo = models.ImageField(
        'Фото', blank=True, null=True, upload_to='media/articles/%Y/%m/')
    title = models.CharField(
        'Заголовок', max_length=255, blank=False, null=False)
    text = models.TextField(
        'Текст статьи', max_length=25000, blank=False, null=False)
    data = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class News(models.Model):
    photo = models.ImageField(
        'Фото', blank=False, null=False, upload_to='media/news/%Y/%m/')
    title = models.CharField(
        'Заголовок', max_length=255, blank=False, null=False)
    text = models.TextField(
        'Текст новости', max_length=25000, blank=False, null=False)
    data = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Laws(models.Model):
    photo = models.ImageField(
        'Фото', blank=False, null=False, upload_to='media/laws/%Y/%m/')
    title = models.CharField(
        'Заголовок', max_length=255, blank=False, null=False)
    text = models.TextField(
        'Текст новости', max_length=25000, blank=False, null=False)
    data = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("laws_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Закон'
        verbose_name_plural = 'Законы'


class Contact(models.Model):
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField('Email', max_length=255)
    phone = models.CharField('Телефон', max_length=255)
    message = models.TextField('Сообщение', blank=True, max_length=10000)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение из формы'
        verbose_name_plural = 'Сообщения из формы'

    def __str__(self) -> str:
        return self.email
