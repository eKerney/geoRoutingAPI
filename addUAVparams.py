from typing import Union
import json

class addUAVparams:
    def __init__(self, GeoJSONinput: Union[dict, str], z_units: str, agl: float, cruiseSpeed: float, firmwareType: float, 
                 hoverSpeed: float, vehicleType: str, version: float):
        self.GeoJSONinput, self.z_units, self.agl, self.cruiseSpeed = GeoJSONinput, z_units, agl, cruiseSpeed
        self.firmwareType, self.hoverSpeed, self.vehicleType, self.version =  firmwareType, hoverSpeed, vehicleType, version
    
    def loadGeoJSONfile(self):
        f = open(self.GeoJSONinput)
        self.GeoJSON = json.load(f)
        print(f'Loaded GeoJSON: {self.GeoJSONinput}')

    def loadGeoJSONdata(self):
        self.GeoJSON = self.GeoJSONinput
        print(f'Loaded GeoJSON: {self.GeoJSONinput}')
    
    def addParams(self):
        #for i, feature in enumerate(self.GeoJSON['features']):
        self.GeoJSON['properties']['z_units'], self.GeoJSON['properties']['agl'] = self.z_units, self.agl 
        self.GeoJSON['properties']['cruiseSpeed'], self.GeoJSON['properties']['firmwareType'] = self.cruiseSpeed, self.firmwareType
        self.GeoJSON['properties']['hoverspeed'], self.GeoJSON['properties']['vehicleType'] = self.hoverSpeed, self.vehicleType 
        self.GeoJSON['properties']['version'] = self.version
        self.GeoJSON['properties']['homeCoords'] = [self.GeoJSON['geometry']['coordinates'][0][1],
                                                self.GeoJSON['geometry']['coordinates'][0][0], self.agl]
        return self.GeoJSON 
