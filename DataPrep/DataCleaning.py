import pandas as pg
import geopandas as gpd

dir = "/Users/sebastian/SkiNavApp/"

filename = "runs.geojson"
file = open(filename)
gdf_runs = gpd.read_file(file)
gdf_runs.head()
