# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
#from django.urls import reverse

class RouteModelOutputPoints(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    geoidheight = models.FloatField(null=True)
    terrainnavd88 = models.FloatField(null=True)
    terrainwgs84 = models.FloatField(null=True)
    units = models.CharField(max_length=5, null=True)
    altitude = models.FloatField(null=True)
    agl = models.FloatField(null=True)
    height_above_takeoff = models.FloatField(null=True)
    geom = models.PointField(srid=4326, null=True)

    def __str__(self):
        return str(self.objectid)

# Auto-generated `LayerMapping` dictionary for RouteModelOutputPoints model
routemodeloutputpoints_mapping = {
    'id': 'id',
    'geoidheight': 'geoidHeight',
    'terrainnavd88': 'terrainNAVD88',
    'terrainwgs84': 'terrainWGS84',
    'units': 'units',
    'altitude': 'altitude',
    'agl': 'AGL',
    'height_above_takeoff': 'height_above_takeoff',
    'geom': 'POINT',
}

class RouteModelLineString(models.Model):
    objectid = models.IntegerField(null=True)
    pathcost = models.FloatField(null=True)
    destid = models.IntegerField(null=True)
    startid = models.IntegerField(null=True)
    shape_length = models.FloatField(null=True)
    geom = models.LineStringField(srid=4326, null=True)  

    def __str__(self):
        return str(self.objectid)


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

class UAVrouteInput(models.Model):
    objectid = models.IntegerField(null=True)
    pathcost = models.FloatField(null=True)
    destid = models.IntegerField(null=True)
    startid = models.IntegerField(null=True)
    shape_length = models.FloatField(null=True)
    geom = models.MultiLineStringField(srid=4326, null=True)  

    def __str__(self):
        return str(self.objectid)

# Auto-generated `LayerMapping` dictionary for UAVrouteInput model
uavrouteinput_mapping = {
    'objectid': 'OBJECTID',
    'pathcost': 'PathCost',
    'destid': 'DestID',
    'startid': 'StartID',
    'shape_length': 'Shape_Length',
    'inline_fid': 'InLine_FID',
    'simlnflag': 'SimLnFlag',
    'maxsimptol': 'MaxSimpTol',
    'minsimptol': 'MinSimpTol',
    'geom': 'MULTILINESTRING',
}

# class RouteModelOutputPoints(models.Model):
#     id = models.CharField(max_length=36, primary_key=True)
#     geoidheight = models.FloatField(null=True)
#     terrainnavd88 = models.FloatField(null=True)
#     terrainwgs84 = models.FloatField(null=True)
#     units = models.CharField(max_length=5, null=True)
#     altitude = models.FloatField(null=True)
#     agl = models.FloatField(null=True)
#     height_above_takeoff = models.FloatField(null=True)
#     cruiseSpeed = models.FloatField(null=True)
#     firmwareType = models.FloatField(null=True)
#     hoverSpeed = models.FloatField(null=True)
#     vehicleType = models.FloatField(null=True)
#     version = models.FloatField(null=True)
#     homeCoords = models.CharField(max_length=84, null=True)
#     geom = models.PointField(srid=4326, null=True)

#     def __str__(self):
#         return str(self.objectid)