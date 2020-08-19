from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import SaoPaulo
from .models import Municipios


class HomePageView(TemplateView):
    template_name = 'index.html'


def saopaulo_datasets(requests):
    state = serialize('geojson', SaoPaulo.objects.all())
    return HttpResponse(state, content_type='json')


def municipios_datasets(requests):
    municipalities = serialize('geojson', Municipios.objects.all())
    return HttpResponse(municipalities, content_type='json')
