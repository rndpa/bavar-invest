from django.contrib import admin
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Flat)
class Flat(admin.ModelAdmin):
    list_display = ('title', 'get_main_photo', 'main_status')
    list_display_links = ('title',)
    readonly_fields = (
        'get_main_photo',
        'get_photo1',
        'get_photo2',
        'get_photo3',
        'get_photo4',
        'get_photo5',
        'get_photo6',
        'get_photo7',
        'get_photo8',
        'get_photo9',
        'get_photo10',
        'get_photo11',
        'get_photo12',
        'get_photo13',
        'get_photo14',
        'get_photo15',
        'get_photo16',
        'get_photo17',
        'get_photo18',
        'get_photo19',
        'get_photo20',
        'get_photo21',
        'get_photo22',
        'get_photo23',
        'get_photo24',
        'get_photo25',
        'get_photo26',
        'get_photo27',
        'get_photo28',
        'get_photo29',
        'get_photo30',
        'get_photo31',
        'get_photo32',
        'get_photo33',
        'get_photo34',
        'get_photo35',
    )

    fieldsets = (
        ('Название объекта', {
            "fields": (
                ('title', 'title_ru', 'title_en',
                 'title_tr', 'title_ar', 'title_fa',)
            ),
        }),
        ('Основные данные', {
            "fields": (
                ('price', 'square',
                 'year_of_construction', 'main_rooms', 'main_type_real_estate', 'main_status', 'main_infrastructure')
            ),
        }),
        ('Расстояния', {
            "fields": (
                ('to_sea', 'to_center', 'to_airport',)
            ),
        }),
        ('Описание объекта недвижимости', {
            "fields": (
                ('description', 'description_ru', 'description_en',
                 'description_tr', 'description_ar', 'description_fa',)
            ),
        }),
        ('Где находится объект', {
            "fields": (
                ('main_country', 'main_district', 'main_city')
            ),
        }),
        ('Предложения по категориям', {
            "fields": (
                ('main_offer', 'hot_offer', 'first_line', 'out_infra', 'vip')
            ),
        }),
        ('Дополнительные параметры объекта', {
            "fields": (
                ('wireless_Internet', 'billiard', 'electric_generator', 'Green_Garden', 'finnish_sauna', 'jacuzzi',
                 'playground', 'video_surveillance', 'table_tennis', 'indoor_swimming_pool', 'roman_Steam_Room',
                 'satellite_TV', 'massage_rooms', 'fitness_center', 'turkish_hamam', 'play_room', 'children_pool',
                 'outdoor_swimming_pool', 'gazebos_for_recreation', 'covered_parking', 'outdoor_parking')
            ),
        }),
        ('Главное фото', {
            "fields": (
                ('get_main_photo', 'main_photo',)
            ),
        }),
        ('Фото 1', {
            "fields": (
                ('get_photo1', 'photo1',)
            ),
        }),
        ('Фото 2', {
            "fields": (
                ('get_photo2', 'photo2',)
            ),
        }),
        ('Фото 3', {
            "fields": (
                ('get_photo3', 'photo3',)
            ),
        }),
        ('Фото 4', {
            "fields": (
                ('get_photo4', 'photo4',)
            ),
        }),
        ('Фото 5', {
            "fields": (
                ('get_photo5', 'photo5',)
            ),
        }),
        ('Фото 6', {
            "fields": (
                ('get_photo6', 'photo6',)
            ),
        }),
        ('Фото 7', {
            "fields": (
                ('get_photo7', 'photo7',)
            ),
        }),
        ('Фото 8', {
            "fields": (
                ('get_photo8', 'photo8',)
            ),
        }),
        ('Фото 9', {
            "fields": (
                ('get_photo9', 'photo9',)
            ),
        }),
        ('Фото 10', {
            "fields": (
                ('get_photo10', 'photo10',)
            ),
        }),
        ('Фото 11', {
            "fields": (
                ('get_photo11', 'photo11',)
            ),
        }),
        ('Фото 12', {
            "fields": (
                ('get_photo12', 'photo12',)
            ),
        }),
        ('Фото 13', {
            "fields": (
                ('get_photo13', 'photo13',)
            ),
        }),

        ('Фото 14', {
            "fields": (
                ('get_photo14', 'photo14',)
            ),
        }),
        ('Фото 15', {
            "fields": (
                ('get_photo15', 'photo15',)
            ),
        }),
        ('Фото 16', {
            "fields": (
                ('get_photo16', 'photo16',)
            ),
        }),
        ('Фото 17', {
            "fields": (
                ('get_photo17', 'photo17',)
            ),
        }),
        ('Фото 18', {
            "fields": (
                ('get_photo18', 'photo18',)
            ),
        }),
        ('Фото 19', {
            "fields": (
                ('get_photo19', 'photo19',)
            ),
        }),
        ('Фото 20', {
            "fields": (
                ('get_photo20', 'photo20',)
            ),
        }),
        ('Фото 21', {
            "fields": (
                ('get_photo21', 'photo21',)
            ),
        }),
        ('Фото 22', {
            "fields": (
                ('get_photo22', 'photo22',)
            ),
        }),
        ('Фото 23', {
            "fields": (
                ('get_photo23', 'photo23',)
            ),
        }),
        ('Фото 24', {
            "fields": (
                ('get_photo24', 'photo24',)
            ),
        }),
        ('Фото 25', {
            "fields": (
                ('get_photo25', 'photo25',)
            ),
        }),
        ('Фото 26', {
            "fields": (
                ('get_photo26', 'photo26',)
            ),
        }),
        ('Фото 27', {
            "fields": (
                ('get_photo27', 'photo27',)
            ),
        }),
        ('Фото 28', {
            "fields": (
                ('get_photo28', 'photo28',)
            ),
        }),
        ('Фото 29', {
            "fields": (
                ('get_photo29', 'photo29',)
            ),
        }),
        ('Фото 30', {
            "fields": (
                ('get_photo30', 'photo30',)
            ),
        }),
        ('Фото 31', {
            "fields": (
                ('get_photo31', 'photo31',)
            ),
        }),
        ('Фото 32', {
            "fields": (
                ('get_photo32', 'photo32',)
            ),
        }),
        ('Фото 33', {
            "fields": (
                ('get_photo33', 'photo33',)
            ),
        }),
        ('Фото 34', {
            "fields": (
                ('get_photo34', 'photo34',)
            ),
        }),
        ('Фото 35', {
            "fields": (
                ('get_photo35', 'photo35',)
            ),
        }),
        ('Служебные данные', {
            "fields": (
                ('slug',)
            ),
        }),
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},
    }

    def get_main_photo(self, obj):
        return mark_safe(f'<img src="{obj.main_photo.url}" width=100 height=100')

    get_main_photo.short_description = 'Главное фото'

    def get_photo1(self, obj):
        return mark_safe(f'<img src="{obj.photo1.url}" width=100 height=100')

    get_photo1.short_description = 'Фото 1'

    def get_photo2(self, obj):
        return mark_safe(f'<img src="{obj.photo2.url}" width=100 height=100')

    get_photo2.short_description = 'Фото 2'

    def get_photo3(self, obj):
        return mark_safe(f'<img src="{obj.photo3.url}" width=100 height=100')

    get_photo3.short_description = 'Фото 3'

    def get_photo4(self, obj):
        return mark_safe(f'<img src="{obj.photo4.url}" width=100 height=100')

    get_photo4.short_description = 'Фото 4'

    def get_photo5(self, obj):
        return mark_safe(f'<img src="{obj.photo5.url}" width=100 height=100')

    get_photo5.short_description = 'Фото 5'

    def get_photo6(self, obj):
        return mark_safe(f'<img src="{obj.photo6.url}" width=100 height=100')

    get_photo6.short_description = 'Фото 6'

    def get_photo7(self, obj):
        return mark_safe(f'<img src="{obj.photo7.url}" width=100 height=100')

    get_photo7.short_description = 'Фото 7'

    def get_photo8(self, obj):
        return mark_safe(f'<img src="{obj.photo8.url}" width=100 height=100')

    get_photo8.short_description = 'Фото 8'

    def get_photo9(self, obj):
        return mark_safe(f'<img src="{obj.photo9.url}" width=100 height=100')

    get_photo9.short_description = 'Фото 9'

    def get_photo10(self, obj):
        return mark_safe(f'<img src="{obj.photo10.url}" width=100 height=100')

    get_photo10.short_description = 'Фото 10'

    def get_photo11(self, obj):
        return mark_safe(f'<img src="{obj.photo11.url}" width=100 height=100')

    get_photo11.short_description = 'Фото 11'

    def get_photo12(self, obj):
        return mark_safe(f'<img src="{obj.photo12.url}" width=100 height=100')

    get_photo12.short_description = 'Фото 12'

    def get_photo13(self, obj):
        return mark_safe(f'<img src="{obj.photo13.url}" width=100 height=100')

    get_photo13.short_description = 'Фото 13'

    def get_photo14(self, obj):
        return mark_safe(f'<img src="{obj.photo14.url}" width=100 height=100')

    get_photo14.short_description = 'Фото 14'

    def get_photo15(self, obj):
        return mark_safe(f'<img src="{obj.photo15.url}" width=100 height=100')

    get_photo15.short_description = 'Фото 15'

    def get_photo16(self, obj):
        return mark_safe(f'<img src="{obj.photo16.url}" width=100 height=100')

    get_photo16.short_description = 'Фото 16'

    def get_photo17(self, obj):
        return mark_safe(f'<img src="{obj.photo17.url}" width=100 height=100')

    get_photo17.short_description = 'Фото 17'

    def get_photo18(self, obj):
        return mark_safe(f'<img src="{obj.photo18.url}" width=100 height=100')

    get_photo18.short_description = 'Фото 18'

    def get_photo19(self, obj):
        return mark_safe(f'<img src="{obj.photo19.url}" width=100 height=100')

    get_photo19.short_description = 'Фото 19'

    def get_photo20(self, obj):
        return mark_safe(f'<img src="{obj.photo20.url}" width=100 height=100')

    get_photo20.short_description = 'Фото 20'

    def get_photo21(self, obj):
        return mark_safe(f'<img src="{obj.photo21.url}" width=100 height=100')

    get_photo21.short_description = 'Фото 21'

    def get_photo22(self, obj):
        return mark_safe(f'<img src="{obj.photo22.url}" width=100 height=100')

    get_photo22.short_description = 'Фото 22'

    def get_photo23(self, obj):
        return mark_safe(f'<img src="{obj.photo23.url}" width=100 height=100')

    get_photo23.short_description = 'Фото 23'

    def get_photo24(self, obj):
        return mark_safe(f'<img src="{obj.photo24.url}" width=100 height=100')

    get_photo24.short_description = 'Фото 24'

    def get_photo25(self, obj):
        return mark_safe(f'<img src="{obj.photo25.url}" width=100 height=100')

    get_photo25.short_description = 'Фото 25'

    def get_photo26(self, obj):
        return mark_safe(f'<img src="{obj.photo26.url}" width=100 height=100')

    get_photo26.short_description = 'Фото 26'

    def get_photo27(self, obj):
        return mark_safe(f'<img src="{obj.photo27.url}" width=100 height=100')

    get_photo27.short_description = 'Фото 27'

    def get_photo28(self, obj):
        return mark_safe(f'<img src="{obj.photo28.url}" width=100 height=100')

    get_photo28.short_description = 'Фото 28'

    def get_photo29(self, obj):
        return mark_safe(f'<img src="{obj.photo29.url}" width=100 height=100')

    get_photo29.short_description = 'Фото 29'

    def get_photo30(self, obj):
        return mark_safe(f'<img src="{obj.photo30.url}" width=100 height=100')

    get_photo30.short_description = 'Фото 30'

    def get_photo31(self, obj):
        return mark_safe(f'<img src="{obj.photo31.url}" width=100 height=100')

    get_photo31.short_description = 'Фото 31'

    def get_photo32(self, obj):
        return mark_safe(f'<img src="{obj.photo32.url}" width=100 height=100')

    get_photo32.short_description = 'Фото 32'

    def get_photo33(self, obj):
        return mark_safe(f'<img src="{obj.photo33.url}" width=100 height=100')

    get_photo33.short_description = 'Фото 33'

    def get_photo34(self, obj):
        return mark_safe(f'<img src="{obj.photo34.url}" width=100 height=100')

    get_photo34.short_description = 'Фото 34'

    def get_photo35(self, obj):
        return mark_safe(f'<img src="{obj.photo35.url}" width=100 height=100')

    get_photo35.short_description = 'Фото 35'


@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ('country',)


@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ('city',)


@admin.register(Type_real_estate)
class Type_real_estate(admin.ModelAdmin):
    list_display = ('type_real_estate',)


@admin.register(Rooms)
class Rooms(admin.ModelAdmin):
    list_display = ('rooms',)


@admin.register(Offer)
class Offer(admin.ModelAdmin):
    list_display = ('offer',)


@admin.register(District)
class District(admin.ModelAdmin):
    list_display = ('district',)


@admin.register(Reviews)
class Reviews(admin.ModelAdmin):
    list_display = ('name', 'data', 'text')
    list_display_links = ('name', 'data',)


@admin.register(Articles)
class Articles(admin.ModelAdmin):
    list_display = ('title', 'data', 'text')


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('title', 'data', 'text')


@admin.register(Laws)
class Laws(admin.ModelAdmin):
    list_display = ('title', 'data', 'text')


@admin.register(Status)
class Status(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Infrastructure)
class Infrastructure(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'create_at')


admin.site.site_title = 'Bavar-Invest.com Панель администратора'
admin.site.site_header = 'Bavar-Invest.com'
