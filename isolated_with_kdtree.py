import pandas as pd
import numpy as np
from math import *
from scipy import spatial

def to_Cartesian(lat, lng):
	R = 6367
	x = R * cos(lat) * cos(lng)
	y = R * cos(lat) * sin(lng)
	z = R * sin(lat)
	return x, y, z

def degtorad(degree):
    rad = degree * 2*np.pi / 360
    return(rad)

def inkms(x):
    R = 6367 # earth radius
    gamma = 2*np.arcsin(degtorad(x/(2*R)))
    distance = 2*R*sin(gamma/2) 
    return(distance)


rawdata = pd.read_csv("location to the file")

# convert the geodetic coordinates into 3D catesian coordinates (ECEF = earth-centered, earth-fixed)
rawdata['x'], rawdata['y'], rawdata['z'] = zip(*map(to_Cartesian, rawdata['Latitude'], rawdata['Longitude']))

coordinates = list(zip(rawdata['x'], rawdata['y'], rawdata['z']))
tree = spatial.KDTree(coordinates)

for i in range(len(rawdata)):
	rawdata["nearest_neighbour_distance"] = inkms(tree.query(coordinates[i],2)[0][1])



isolated_palce = rawdata.loc[rawdata["nearest_neighbour_distance"].idxmax()]["LocationId"]

isolated_place_per_each = rawdata.groupby('Country')['nearest_neighbour_distance'].max()


