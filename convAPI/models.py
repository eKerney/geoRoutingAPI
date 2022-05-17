# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
#from django.urls import reverse

class surfaceHex(models.Model):
    index_field = models.CharField(max_length=254, null=True)
    lulc = models.CharField(max_length=254, null=True)
    population = models.FloatField(null=True)
    railroads = models.CharField(max_length=254, null=True)
    schools = models.CharField(max_length=254, null=True)
    uasfm_ceil = models.CharField(max_length=254, null=True)
    h3_index = models.CharField(max_length=254, null=True)
    hospitals = models.CharField(max_length=254, null=True)
    prisons = models.CharField(max_length=254, null=True)
    fcc_asr = models.CharField(max_length=254, null=True)
    roads = models.CharField(max_length=254, null=True)
    transmissi = models.CharField(max_length=254, null=True)
    helipads = models.CharField(max_length=254, null=True)
    stadium = models.CharField(max_length=254, null=True)
    electric_s = models.CharField(max_length=254, null=True)
    police_sta = models.CharField(max_length=254, null=True)
    eocs = models.CharField(max_length=254, null=True)
    airports = models.CharField(max_length=254, null=True)
    wind_farms = models.CharField(max_length=254, null=True)
    uasfm_max = models.FloatField(null=True)
    uasfm_min = models.FloatField(null=True)
    score = models.FloatField(null=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326, null=True)

    def __str__(self):
        return str(self.h3_index)
    
    # def get_absolute_url(self):
    #     return reverse('station-detail',args=[str(self.h3_index)] )

# Auto-generated `LayerMapping` dictionary for surfaceHex model
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