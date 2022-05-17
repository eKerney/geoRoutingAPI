from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import surfaceHex

@admin.register(surfaceHex)
class SurfaceAdmin(OSMGeoAdmin):
    list_display = ('h3_index', 'score')

# Register your models here.
