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
from CARSAPI import CARS
from addUAVparams import addUAVparams
from H3pyTools import H3dataTools
from RouteToKML import RouteToKML
from PlanFile import RouteToPlanSimple

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
    #permission_classes = [permissions.IsAuthenticated]
    
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

        return Response(GeoJSONoutput)

    @action(detail=False, methods=['post'])
    def toGeoJSON(self, request):
        # Input parameters
        data = request.data
        serializer = RouteLineSerializer(data=data[0])
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        z_units, agl = 'm', 100
        plan = CARS(serializer.data, z_units, agl)
        GeoJSONoutput = plan.runGeoTool()

        return Response(GeoJSONoutput)
    
    @action(detail=False, methods=['post'])
    def toGeoJSONuav(self, request):
        # Input parameters
        data = request.data
        serializer = RouteLineSerializer(data=data[0])
        if serializer.is_valid():
           serializer.save()
        else:
           return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
        addedParams = addUAVparams(serializer.data, data[1]['z_units'], data[1]['agl'], data[1]['cruiseSpeed'], 
        data[1]['firmwareType'], data[1]['hoverSpeed'],data[1]['vehicleType'],data[1]['version'])
        #Run Process
        addedParams.loadGeoJSONdata()
        GeoJSON = addedParams.addParams()

        CARSgeo = CARS(GeoJSON, data[1]['z_units'], data[1]['agl'], data[1]['cruiseSpeed'], data[1]['firmwareType'], 
        data[1]['hoverSpeed'],data[1]['vehicleType'], data[1]['version'], GeoJSON['properties']['homeCoords'])
        GeoJSONoutput = CARSgeo.runGeoTool()

        return Response(GeoJSONoutput)
    
    @action(detail=False, methods=['post'])
    def toH3Traversal(self, request):
        # Input parameters
        data = request.data
        newGeo = H3dataTools(data[0], data[1]['hexRes'])
        #newGeo.loadGeoJSONptsAPI('data\\MDOT_MCS_FWH_H3')
        newGeo.geoPointstoH3traverse()

        return Response(newGeo.geojson)

    @action(detail=False, methods=['post'])
    def toKMLuav(self, request):
        # Input parameters
        data = request.data
        z_units = 'ft'
        agl = 400
        outputName = 'UAVflightPath'
        # Instantiate RouteToKML class
        routes = RouteToKML(data, z_units, agl, outputName)
        # Run Process
        KMLoutput = routes.runGeoTool()
        return Response(KMLoutput)  
    
    @action(detail=False, methods=['post'])
    def toPlanfile(self, request):
        # Parse request data, data[0]=GeoJSON LineString Feature, data[1]=PlanFile parameters
        data = request.data
        # Add UAV params to GeoJSON LineString, extract home coordinates as first point position
        routeAddUAV = addUAVparams(data[0], data[1]['z_units'], data[1]['agl'], data[1]['cruiseSpeed'], 
        data[1]['firmwareType'], data[1]['hoverSpeed'],data[1]['vehicleType'],data[1]['version'])
        #Run Process
        GeoJSONuav = routeAddUAV.runGeoTool()

        planFileRoute = RouteToPlanSimple(GeoJSONuav, data[1]['z_units'], data[1]['agl'], data[1]['cruiseSpeed'], data[1]['firmwareType'], 
        data[1]['hoverSpeed'],data[1]['vehicleType'], data[1]['version'], GeoJSONuav['properties']['homeCoords'])
        planFileOutput = planFileRoute.runGeoTool()
        return Response(planFileOutput)


class RouteOutputPointsView(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = RouteModelOutputPoints.objects.all()
    serializer_class = RouteOutputPointsSerializer
    permission_classes = [permissions.IsAuthenticated]