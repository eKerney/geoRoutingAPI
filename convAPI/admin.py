from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import RouteModelOutputPoints, surfaceHex, UAVrouteInput, RouteModelLineString

@admin.register(surfaceHex)
class SurfaceAdmin(OSMGeoAdmin):
    list_display = ('h3_index', 'score')

@admin.register(UAVrouteInput)
class UAVrouteInputAdmin(OSMGeoAdmin):
    list_display = ('objectid', 'pathcost')

@admin.register(RouteModelLineString)
class UAVrouteInputAdmin(OSMGeoAdmin):
    list_display = ('objectid', 'pathcost')

@admin.register(RouteModelOutputPoints)
class UAVrouteInputAdmin(OSMGeoAdmin):
    list_display = (['id'])


# Register your models here.
