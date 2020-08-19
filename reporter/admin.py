from django.contrib import admin
from .models import Incidences
from .models import SaoPaulo
from .models import Municipios
from leaflet.admin import LeafletGeoAdmin


class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class SaoPauloAdmin(LeafletGeoAdmin):
    list_display = ('nome', 'uf')


class MunicipiosSPAdmin(LeafletGeoAdmin):
    list_display = ('nm_municip', 'cd_geocodm')


admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(SaoPaulo, SaoPauloAdmin)
admin.site.register(Municipios, MunicipiosSPAdmin)

