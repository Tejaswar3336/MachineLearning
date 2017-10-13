import pandas as pd
from math import radians, cos, sin, asin, sqrt

def haversine(lon1,lat1,lon2,lat2):
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a)) 
	r = 6371
	return c * r


rawdata = pd.read_csv("location of data")

rawdata["nearest_neighbour_distance"] = ""

for i in range(len(rawdata)):
	lon1 = rawdata["Longitude"].loc[i]
	lat1 = rawdata["Latitude"].loc[i]
	distance = []
	for j in range(len(rawdata)):
		lon2 = rawdata["Longitude"].loc[j]
		lat2 = rawdata["Latitude"].loc[j]
		tmp_dist = haversine(lon1,lat1,lon2,lat2)
		distance.append(tmp_dist)

	rawdata["nearest_neighbour_distance"] = sorted(distance)[1]


isolated_palce = rawdata.loc[rawdata["nearest_neighbour_distance"].idxmax()]["LocationId"]

isolated_place_per_each = rawdata.groupby('Country')['nearest_neighbour_distance'].max()

