from django.core.mail import send_mail
from django.http import HttpResponse, HttpRequest

from django.utils.translation import gettext as _

from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

from django.views.generic import ListView, DetailView, CreateView, View, TemplateView

from flat.models import *


class ShowAllView(ListView):
    queryset = Flat.objects.all().order_by('?')
    template_name = 'flat/all.html'
    context_object_name = 'flat'

    reviews = Reviews.objects.all().order_by('?')[:4]
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ShowAllView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowIndexView(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'message']

    flat = Flat.objects.all().order_by('-created_at')[:8]
    reviews = Reviews.objects.all().order_by('?')[:3]
    articles = Articles.objects.all().order_by('-data')[:3]
    news = News.objects.all().order_by('-data')[:4]
    laws = Laws.objects.all().order_by('-data')[:4]
    template_name = 'flat/index.html'
    context_object_name = 'flat'

    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()

    title = 'Bavar-Invest'
    meta_descr = 'Продажа недвижимости в Турции, Грузии, Черногории, Северном Кипре'
    meta_key = 'Купить недвижимость в Турции, Грузии, Черногории, Северном Кипре'
    main_title = 'Купить недвижимость в Турции, Грузии, Черногории, Северном Кипре'
    main_descr = 'Продажа недвижимости в Турции, Грузии, Черногории, Северном Кипре'

    def get_context_data(self, **kwargs):
        context = super(ShowIndexView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['meta_descr'] = self.meta_descr
        context['meta_key'] = self.meta_key
        context['main_title'] = self.main_title
        context['main_descr'] = self.main_descr
        context['flat'] = self.flat
        context['reviews'] = self.reviews
        context['articles'] = self.articles
        context['news'] = self.news
        context['laws'] = self.laws
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]} Телефон: {data["phone"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
    send_mail(subject,
              content,
              '',
              ['']
              )


def success(request):
    return HttpResponse('Письмо отправлено!')


class DetailsFlatView(DetailView):
    queryset = Flat.objects.all()
    template_name = 'flat/details.html'
    context_object_name = 'flat'
    reviews = Reviews.objects.all().order_by('?')[:4]

    def current_name(self):
        return reverse('flat.title')

    def get_context_data(self, **kwargs):
        context = super(DetailsFlatView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class ShowTurkishView(ListView):
    queryset = Flat.objects.all().filter(main_country=1)
    template_name = 'flat/Turkish.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowTurkishView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowChernoView(ListView):
    queryset = Flat.objects.all().filter(main_country=3)
    template_name = 'flat/Cherno.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowChernoView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowGruziaView(ListView):
    queryset = Flat.objects.all().filter(main_country=2)
    template_name = 'flat/gruzia.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowGruziaView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowKiprView(ListView):
    queryset = Flat.objects.all().filter(main_country=4)
    template_name = 'flat/kipr.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowKiprView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowFirstView(ListView):
    queryset = Flat.objects.all().filter(first_line=True)
    template_name = 'flat/offers/first.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowFirstView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowHotView(ListView):
    queryset = Flat.objects.all().filter(hot_offer=True)
    template_name = 'flat/offers/hot.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowHotView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowOutView(ListView):
    queryset = Flat.objects.all().filter(out_infra=True)
    template_name = 'flat/offers/out.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowOutView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowVipView(ListView):
    queryset = Flat.objects.all().filter(vip=True)
    template_name = 'flat/offers/vip.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowVipView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowSobView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=2)
    template_name = 'flat/offers/sob.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowSobView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowZasView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=1)
    template_name = 'flat/offers/zas.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowZasView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowVillView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=8)
    template_name = 'flat/how/villa.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowVillView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowZdaniaView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=6)
    template_name = 'flat/how/zdania.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowZdaniaView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowZemliaView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=3)
    template_name = 'flat/how/zemlia.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowZemliaView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowKvartiraView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=2)
    template_name = 'flat/how/kvartira.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowKvartiraView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowPenthouseView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=5)
    template_name = 'flat/how/penthouse.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowPenthouseView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowKommView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=1)
    template_name = 'flat/how/komm.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowKommView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowTownhouseView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=4)
    template_name = 'flat/how/townhouse.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowTownhouseView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ShowOtelView(ListView):
    queryset = Flat.objects.all().filter(main_type_real_estate=7)
    template_name = 'flat/how/otel.html'
    context_object_name = 'flat'
    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ShowOtelView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ReviewsList(ListView):
    queryset = Reviews.objects.all()
    template_name = 'flat/reviews.html'
    context_object_name = 'reviews'


class ArticlesList(ListView):
    queryset = Articles.objects.all()
    template_name = 'flat/articles.html'
    context_object_name = 'articles'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class ArticlesDetailsList(DetailView):
    queryset = Articles.objects.all()
    template_name = 'flat/articles_detail.html'
    context_object_name = 'articles'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailsList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class NewsList(ListView):
    queryset = News.objects.all()
    template_name = 'flat/news.html'
    context_object_name = 'news'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class NewsDetailList(DetailView):
    queryset = News.objects.all()
    template_name = 'flat/news_detail.html'
    context_object_name = 'news'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(NewsDetailList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class LawsList(ListView):
    queryset = Laws.objects.all()
    template_name = 'flat/laws.html'
    context_object_name = 'laws'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(LawsList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class LawsDetailList(DetailView):
    queryset = Laws.objects.all()
    template_name = 'flat/laws_detail.html'
    context_object_name = 'laws'

    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(LawsDetailList, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class FilterView(ListView):
    queryset = Flat.objects.all()
    template_name = 'flat/filter.html'

    country = Country.objects.all()
    city = City.objects.all()
    district = District.objects.all()
    type_real_estate = Type_real_estate.objects.all()
    reviews = Reviews.objects.all().order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super(FilterView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        context['country'] = self.country
        context['city'] = self.city
        context['district'] = self.district
        context['type_real_estate'] = self.type_real_estate
        return context


class ModalListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        welcome_message = _('Привет мир!')
        return HttpResponse(f'<h1>{welcome_message}</h1>')


class FlatListView(ListModelMixin, GenericAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatListSerializer
    filters_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]
    search_fields = [
        'title',
        'description',

    ]
    filterset_fields = [
        'main_country',
        'main_city',
        'main_district',
        'main_type_real_estate',
        'to_sea',
    ]
    ordering_fields = [
        'title',
        'description',
        'created_at'
    ]

    def get(self, request: Request) -> Response:
        return self.list(request)


# menu

class PolitikaView(TemplateView):
    template_name = 'flat/menu/politika.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(PolitikaView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class CompanyView(TemplateView):
    template_name = 'flat/menu/company.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class ContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'message']
    template_name = 'flat/menu/contact.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class GrazhdanstvoView(TemplateView):
    template_name = 'flat/menu/grazhdanstvo.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(GrazhdanstvoView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class PartnerView(TemplateView):
    template_name = 'flat/menu/partner.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(PartnerView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context


class ServiceView(TemplateView):
    template_name = 'flat/menu/service.html'

    reviews = Reviews.objects.all().order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['reviews'] = self.reviews
        return context
