from django.conf.urls import include
from django.conf.urls import url
from .views import HomePageView
from .views import saopaulo_datasets
from .views import municipios_datasets


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^saopaulo_data/$', saopaulo_datasets, name='state'),
    url(r'^municipios_data/$', municipios_datasets, name='municipalities'),
    url(r'^incidence_data/$', HomePageView.as_view(), name='home'),
]

