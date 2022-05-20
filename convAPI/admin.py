from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import surfaceHex, UAVrouteInput

@admin.register(surfaceHex)
class SurfaceAdmin(OSMGeoAdmin):
    list_display = ('h3_index', 'score')

@admin.register(UAVrouteInput)
class UAVrouteInputAdmin(OSMGeoAdmin):
    list_display = ('objectid', 'pathcost')

# Register your models here.
