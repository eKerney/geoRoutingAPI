from urllib import request
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from convAPI.serializers import UAVgeoJSONserlializer, UserSerializer, GroupSerializer, SurfaceSerializer, UAVrouteInputSerializer, RouteLineSerializer, RouteOutputPointsSerializer
from convAPI.models import surfaceHex, UAVrouteInput, RouteModelLineString, RouteModelOutputPoints
from django.shortcuts import get_object_or_404
import subprocess, sys, os, requests, json, time, pandas as pd
from CARS import CARS

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SurfaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = surfaceHex.objects.all()
    serializer_class = SurfaceSerializer
    permission_classes = [permissions.IsAuthenticated]

class UAVrouteInputViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UAVrouteInput.objects.all()
    serializer_class = UAVrouteInputSerializer
    permission_classes = [permissions.IsAuthenticated]

class UAVgeojsonViewSet(viewsets.ModelViewSet):
    queryset=UAVrouteInput.objects.all()
    serializer_class=UAVgeoJSONserlializer

class UAVgetCARS(viewsets.ModelViewSet):
    print(f'request: {request}')
    queryset = UAVrouteInput.objects.all()
    serializer_class = UAVrouteInputSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        queryset = UAVrouteInput.objects.all()
        serializer = UAVgeoJSONserlializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = UAVrouteInput.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UAVgeoJSONserlializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def getCARSgeoJSON(self, request):
        #print(request.data)
        # Input parameters
        
        serializer = UAVgeoJSONserlializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        last = UAVrouteInput.objects.last()
        serializer = UAVgeoJSONserlializer(last)
        jsonData = JSONRenderer().render(serializer.data)
        jsonLoads = json.loads(jsonData)
        #print(f'current - {json}')

        inputData = 'UAVflightPath_GeoJSON_05052022085651.geojson'
        z_units, agl, outputName = 'm', 30.48, 'UAVplan'
        cruiseSpeed, firmwareType, hoverSpeed, vehicleType, version = 15, 12, 5, 2, 2
        # homeCoords = ]lat, lon, agl]
        homeCoords = [45.650961376465304, 45.650961376465304, 358.68]
        plan = CARS(jsonLoads, z_units, agl, outputName, cruiseSpeed, firmwareType, hoverSpeed, vehicleType, version, homeCoords)
        plan.runGeoTool()

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class RouteModelLineView(viewsets.ModelViewSet):
    print(f'request: {request}')
    queryset = RouteModelLineString.objects.all()
    serializer_class = RouteLineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        queryset = RouteModelLineString.objects.all()
        serializer = RouteLineSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = RouteModelLineString.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RouteLineSerializer(user)

        GeoJSON = { "type": "FeatureCollection", "features": [] }
        GeoJSON["features"].append(serializer.data)
        
        return Response(GeoJSON)
    
    @action(detail=False, methods=['post'])
    def getCARS(self, request):
        #print(request.data)
        # Input parameters
        serializer = RouteLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        last = RouteModelLineString.objects.last()
        serializer = RouteLineSerializer(last)
        jsonData = JSONRenderer().render(serializer.data)
        jsonLoads = json.loads(jsonData)
        #print(f'current - {json}')

        inputData = 'UAVflightPath_GeoJSON_05052022085651.geojson'
        z_units, agl, outputName = 'm', 30.48, 'UAVplan'
        cruiseSpeed, firmwareType, hoverSpeed, vehicleType, version = 15, 12, 5, 2, 2
        # homeCoords = ]lat, lon, agl]
        homeCoords = [45.650961376465304, 45.650961376465304, 358.68]
        plan = CARS(jsonLoads, z_units, agl, outputName, cruiseSpeed, firmwareType, hoverSpeed, vehicleType, version, homeCoords)
        GeoJSONoutput = plan.runGeoTool()
        # GeoJSON = { "type": "FeatureCollection", "features": [] }
        # GeoJSON["features"].append(serializer.data)

        return Response(GeoJSONoutput, status=status.HTTP_200_OK)
    
class RouteOutputPointsView(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = RouteModelOutputPoints.objects.all()
    serializer_class = RouteOutputPointsSerializer
    permission_classes = [permissions.IsAuthenticated]