import os
from django.contrib.gis.utils import LayerMapping
from .models import surfaceHex

# Each key in the administrativelevel2boundaries_mapping dictionary corresponds to
# a field in the AdministrativeLevel2Boundaries model.
surfacehex_mapping = {
    'index_field': 'index_',
    'lulc': 'lulc',
    'population': 'population',
    'railroads': 'railroads',
    'schools': 'schools',
    'uasfm_ceil': 'uasfm_ceil',
    'h3_index': 'h3_index',
    'hospitals': 'hospitals',
    'prisons': 'prisons',
    'fcc_asr': 'fcc_asr',
    'roads': 'roads',
    'transmissi': 'transmissi',
    'helipads': 'helipads',
    'stadium': 'stadium',
    'electric_s': 'electric_s',
    'police_sta': 'police_sta',
    'eocs': 'eocs',
    'airports': 'airports',
    'wind_farms': 'wind_farms',
    'uasfm_max': 'uasfm_max',
    'uasfm_min': 'uasfm_min',
    'score': 'Score',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

tha_adm2_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'mdotSurface.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        surfaceHex, tha_adm2_shp, surfacehex_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)
