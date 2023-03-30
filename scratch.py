import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


site_locations = pd.read_csv('data/LOCAR_Site_Information.csv',
                             skipfooter=11, engine='python',
                             usecols = ['Site Code', 'Easting', 'Northing'],
                             index_col='Site Code')
site_geometry = gpd.points_from_xy(site_locations['Easting'],
                                   site_locations['Northing'], crs='EPSG:27700')
site_gdf = gpd.GeoDataFrame(site_locations, geometry=site_geometry)
site_gdf
site_gdf.crs

site_gdf_ll = site_gdf.to_crs('EPSG:4326')
site_gdf_ll
site_gdf_ll.crs


FP_catchment = gpd.GeoDataFrame.from_file('data/river_catchments/frome_piddle_catchment.shp')

FP_sites = gpd.sjoin(site_gdf, FP_catchment)

FP_sites

PL_catchment = gpd.GeoDataFrame.from_file('data/river_catchments/pang_lambourn_catchment.shp')
PL_sites = gpd.sjoin(site_gdf, PL_catchment)
PL_sites['index_right']

PL_catchment.plot()
plt.show()



def is_site_within_catchment(site_dataframe, catchment_dataframe):
    answer_dataframe = gpd.sjoin(site_dataframe, catchment_dataframe)
    if answer_dataframe.size:
        return True
    else:
        return False

is_site_within_catchment(site_gdf_ll.loc[['FP23']],PL_catchment)
is_site_within_catchment(site_gdf_ll.loc[['FP23']],FP_catchment)
#this doesn't give the right answer

type(site_gdf.loc['FP23'])
type(site_gdf.loc[['FP23']])

garea = gpd.GeoDataFrame(
                geometry = [Polygon([(0, 10), (10, 10), (10, 0), (0, 0)])],
                crs = 'EPSG:4326')
gpoint = gpd.GeoDataFrame(geometry=[Point((5,5))],crs='EPSG:4326')