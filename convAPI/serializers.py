from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from django.contrib.gis import serializers
from convAPI.models import surfaceHex, UAVrouteInput, RouteModelLineString, RouteModelOutputPoints
from django.core.serializers import serialize
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = surfaceHex
        fields = '__all__'

class UAVrouteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAVrouteInput
        fields = '__all__'

class UAVgeoJSONserlializer(GeoFeatureModelSerializer):
    class Meta:
        model = UAVrouteInput
        geo_field = "geom"
        fields = '__all__'

class RouteLineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteModelLineString
        geo_field = "geom"
        fields = '__all__'

class RouteOutputPointsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteModelOutputPoints
        geo_field = "geom"
        fields = '__all__'