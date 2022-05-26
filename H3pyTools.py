from typing import Union
import pandas as pd
import h3
import json
import time

class H3dataTools:
    def __init__(self, inputPath: Union[dict, str], res: int):
        self.inputPath, self.res = inputPath, res      

    def loadCSV(self, col: list, numRec: int, props: list, outName: str):
        '''Loads GeoJSON file generated from :class:'CostPathFromSurface' class
        :return: Prints success message with name of loaded GeoJSON e.g.
        Loaded GeoJSON: pendleOR_GeoJSON_17032022144129.geojson
        :rtype: none
        '''
        self.col, self.numRec, self.props, self.outName = col, numRec, props, outName         
        file = open(self.inputPath)
        self.CSVlines = len(file.readlines())
        print (self.CSVlines)
        for x, i in enumerate(range(0, self.CSVlines, self.numRec)):    
            if x == 0:
                self.df = pd.read_csv(self.inputPath, skiprows=i, nrows=self.numRec)
            else:
                self.df = pd.read_csv(self.inputPath, header=None, names=self.col, skiprows=i, nrows=self.numRec)
            print(f'Loaded CSV rows: {i} - {i + self.numRec}')
            self.convertH3()
            self.saveGeoJSON()

     # Load raw GeoJSON file as JSON     
    def loadGeoJSONptsAPI(self, outName: str):
        '''Loads GeoJSON Points Path for use in GeoRouting Conversion API
        Loads GeoJSON file generated from :class:'CostPathFromSurface' class
        GeoJSON is further processed by CARS.py to generate both GeoJSON LineString & GeoJSON Points
        The H3 conversion functions will retain the attributes of the GeoJSON Points 
        :return: Prints success message with name of loaded GeoJSON data
        :rtype: none
        ''' 
        self.outName = outName         
        self.loadedGeoJSON = self.inputPath
        print(f'Loaded GeoJSON: ')
    
       # Load raw GeoJSON file as JSON     
    def loadGeoJSONpts(self, outName: str):
        '''Loads GeoJSON Points Path for use in GeoRouting Conversion Notebooks and Scripts 
        Loads GeoJSON file generated from :class:'CostPathFromSurface' class
        GeoJSON is further processed by CARS.py to generate both GeoJSON LineString & GeoJSON Points
        The H3 conversion functions will retain the attributes of the GeoJSON Points 
        :return: Prints success message with name of loaded GeoJSON data
        :rtype: none
        '''       
        self.outName = outName 
        f = open(self.inputPath)
        self.loadedGeoJSON = json.load(f)
        print(f'Loaded GeoJSON: {self.inputPath}')
    
    def geoPointstoH3traverse(self):
        self.geojson = {'type':'FeatureCollection', 'features':[]}
        arrLength = len(self.loadedGeoJSON['features'])
        for i, feature in enumerate(self.loadedGeoJSON['features']):
            h3Current = h3.geo_to_h3(feature['geometry']['coordinates'][1], 
            feature['geometry']['coordinates'][0], self.res)

            if arrLength - 1 != i:
                h3Next = h3.geo_to_h3(self.loadedGeoJSON['features'][i+1]['geometry']['coordinates'][1], 
                self.loadedGeoJSON['features'][i+1]['geometry']['coordinates'][0], self.res)
            else:
                h3Next = h3.geo_to_h3(self.loadedGeoJSON['features'][i]['geometry']['coordinates'][1], 
                self.loadedGeoJSON['features'][i]['geometry']['coordinates'][0], self.res)
            hexLine = h3.h3_line(h3Next, h3Current)

            for i, z in enumerate(hexLine):
                geom = h3.h3_to_geo_boundary(z, True)
                feature = { "type": "Feature", "properties": feature['properties'], 
                "geometry": { "type": "Polygon", "coordinates": [geom]} }
                self.geojson['features'].append(feature)

    
    def convertH3(self):
        self.geojson = {'type':'FeatureCollection', 'features':[]}
        for _, row in self.df.iterrows():
            coords = h3.h3_to_geo_boundary(row['H3'], geo_json=True)
            # template for each feature
            feature = {'type':'Feature',
                        'properties':{},
                    'geometry':{'type':'Polygon',
                                'coordinates':[coords]}}
            #feature['geometry']['coordinates'] = [coords]
            # add each column as GeoJSON property
            for prop in self.props:
                feature['properties'][prop] = row[prop]
            # append feature to Feature Collection
            self.geojson['features'].append(feature)
        print(f'Created GeoJSON dictonary from dataframe')

    def saveGeoJSON(self):
        '''_summary_
        '''      
        # serialize GeoJSON object
        self.json_object = json.dumps(self.geojson, indent = 4)
        # create file timestamp
        self.timeStamp = time.strftime('%d%m%Y%H%M%S')
        # write GeoJSON output file
        with open((f'{self.outName}_{self.timeStamp}.geojson'), "w") as outfile:
            outfile.write(self.json_object)
        print(f'GeoJSON output: {self.outName}_{self.timeStamp}.geojson')
