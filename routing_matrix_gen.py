import re
import requests
import json
import pandas
import os
import core_tools as ct
#endpoint = "https://valhalla.mapzen.com/matrix"
mapzen_endpoint = "https://matrix.mapzen.com/many_to_many"

####import your API key from mapzen
def import_mapzen_key(fname):
    key = 'mapzen-yourkey'
    with open('fname', 'r') as f: ####key in a file
        key = f.readline()
        key = re.sub('\s+','',key)
    return key


def example_query():
    path=json.dumps({"locations":[{"lat":40.744014,"lon":-73.990508},{"lat":40.739735,"lon":-73.979713},{"lat":40.752522,"lon":-73.985015},{"lat":40.750117,"lon":-73.983704},{"lat":40.750552,"lon":-73.993519}], "costing":"auto"})
    #params = {"json": json.dumps(route), "api_key": key}
    params = {"json":path,"api_key":key}
    req = requests.get(endpoint, params=params)
    print(req.text)

### demo less than 50x50 matrix
def mapzen_small_demo(eg_fname1="example1.csv",data_folder="data",data_out_folder="dataOut",key_file="key.txt"):
    key = import_mapzen_key(key_file)
    filename = eg_fname1 ##csv with less than 50x50 options
    ct.create_dir(data_folder)
    ct.create_dir(data_out_folder)

    dataIn = pandas.read_csv(data_folder+"/"+filename)
    dataIn.head()
    locations = []
    for i in range(len(dataIn.index)):
        locations.append({"lon":dataIn.Lon.iloc[i], "lat":dataIn.Lat.iloc[i]})

    test1 = locations
    ## Specify transport mode
    #- auto (car)
    #- pedestrian
    #- bicyle
    costing = "auto"
    dictPath = {"locations":locations, "costing":costing}
    path = json.dumps(dictPath)
    params = {"json":path,"api_key":key}
    req = requests.get(endpoint, params=params)

    jsonback = req.json()
    locationsOut = jsonback.get("locations")
    rawMatrix = jsonback.get("many_to_many")
    cols = list(range(1, 51))
    mo = pandas.DataFrame(columns=cols, index = cols)
    for row in rawMatrix:
    for edge in row:
        D = edge['to_index']
        O = edge['from_index']
        distance = edge['distance']
        mo.iloc[D,O]= distance
    mo.head()

    mo.to_csv("dataOut/"+filename)


def mapzen_large_demo(eg_fname1="example1.csv",data_folder="data",data_out_folder="dataOut",key_file="key.txt"):
    pass
