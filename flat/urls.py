from django.urls import path, include

from django.conf.urls.static import static
from alanya_invest import settings
from flat.views import *

urlpatterns = [
    path('', ShowIndexView.as_view(), name='home'),

    path('all', ShowAllView.as_view(), name='all'),
    path('filter', FilterView.as_view(), name='filter'),

    path('turkish', ShowTurkishView.as_view(), name='turkish'),
    path('cherno', ShowChernoView.as_view(), name='cherno'),
    path('gruzia', ShowGruziaView.as_view(), name='gruzia'),
    path('kipr', ShowKiprView.as_view(), name='kipr'),

    path('first_line', ShowFirstView.as_view(), name='first_line'),
    path('hot_offer', ShowHotView.as_view(), name='hot_offer'),
    path('out_infra', ShowOutView.as_view(), name='out_infra'),
    path('vip', ShowVipView.as_view(), name='vip'),
    path('sob', ShowSobView.as_view(), name='sob'),
    path('zas', ShowZasView.as_view(), name='zas'),

    path('villa', ShowVillView.as_view(), name='villa'),
    path('zdania', ShowZdaniaView.as_view(), name='zdania'),
    path('zemlia', ShowZemliaView.as_view(), name='zemlia'),
    path('kvartira', ShowKvartiraView.as_view(), name='kvartira'),
    path('penthouse', ShowPenthouseView.as_view(), name='penthouse'),
    path('komm', ShowKommView.as_view(), name='komm'),
    path('townhouse', ShowTownhouseView.as_view(), name='townhouse'),
    path('otel', ShowOtelView.as_view(), name='otel'),

    path('reviews', ReviewsList.as_view(), name='reviews'),
    path('articles', ArticlesList.as_view(), name='articles'),
    path('news', NewsList.as_view(), name='news'),
    path('laws', LawsList.as_view(), name='laws'),
    
    path('politika', PolitikaView.as_view(), name='politika'),
    path('company', CompanyView.as_view(), name='company'),
    path('contact', ContactView.as_view(), name='contact'),
    path('grazhdanstvo', GrazhdanstvoView.as_view(), name='grazhdanstvo'),
    # path('partner', PartnerView.as_view(), name='partner'),
    path('service', ServiceView.as_view(), name='service'),
    

    path('flat', FlatListView.as_view(), name='flat'),

    path('<pk>', DetailsFlatView.as_view(), name='details'),
    path('articles/<pk>', ArticlesDetailsList.as_view(), name='articles_details'),
    path('news/<pk>', NewsDetailList.as_view(), name='news_details'),
    path('laws/<pk>', LawsDetailList.as_view(), name='laws_details'),

    path('i18n', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
