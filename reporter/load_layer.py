import os
from django.contrib.gis.utils import LayerMapping
from .models import SaoPaulo
from .models import Municipios

saopaulo_mapping = {
    'uf': 'UF',
    'nome': 'Nome',
    'geom': 'MULTIPOLYGON',
}
saopaulo_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/sao_paulo.shp'))

municipios_mapping = {
    'id': 'ID',
    'cd_geocodm': 'CD_GEOCODM',
    'nm_municip': 'NM_MUNICIP',
    'geom': 'MULTIPOLYGON',
}
municipios_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/municipios_sp.shp'))


def run(verbose=True):
    lm_sp = LayerMapping(SaoPaulo, saopaulo_shp, saopaulo_mapping, transform=False, encoding='iso-8859-1')
    lm_mn = LayerMapping(Municipios, municipios_shp, municipios_mapping, transform=False, encoding='iso-8859-1')
    lm_sp.save(strict=True, verbose=True)
    lm_mn.save(strict=True, verbose=True)
