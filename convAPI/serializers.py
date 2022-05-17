from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from django.contrib.gis import serializers
from convAPI.models import surfaceHex

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SurfaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = surfaceHex
        fields = ['h3_index', 'score']

