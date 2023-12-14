from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('district',)


@register(Type_real_estate)
class Type_real_estateTranslationOptions(TranslationOptions):
    fields = ('type_real_estate',)


@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('offer',)


@register(Status)
class StatusTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Infrastructure)
class InfrastructureTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Laws)
class LawsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Flat)
class FlatTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
