import processing
import time

def reproject_crs(lyr1, change_crs):
    #Reproject layers.
    #Parameters:
    #lyr1 : shapefile//path
    #The name/path of the layer to be reprojected
    #change_crs : string of the new CRS
    #(Uses temp layers to reduce memory consumption)
    print(lyr1,change_crs)
    rp = processing.run('native:reprojectlayer',
    {'INPUT': lyr1,
    'TARGET_CRS': change_crs,
    'OUTPUT': 'memory:Reprojected'}
    )
    return rp

def clipping(lyr1, lyr2):
    #Run clip tool.
    #Parameters:
    #lyr1 : shapefile//path
    #The name of the input shapefile to be clipped
    #lyr2 : path to vector data
    #The name of the overlay area
    layer_clip = processing.run('qgis:clip',
        {'INPUT': lyr1,
        'OVERLAY': lyr2,
        'OUTPUT': 'memory:Clipped'}
    )
    return layer_clip

def buff_points(static_dis, lyr):
    #Run buffer tool on clipped points.
    #Parameters:
    #static_dis : shapefile//path
    #The value used to buffer by (distance)
    #lyr : shapefile//path
    #The name of the input shapefile to buffer
    #lyr2 : shapefile//path
    #The name of the output path
    buff = processing.run('native:buffer',
        {'INPUT': lyr,
        'DISTANCE':static_dis,
        'OUTPUT': 'memory:2kmBuffed'}
    )
    return buff

start_time = time.time()
#Set input and output file paths
on_dam_path = r"M:\School\4YP3\DS\Data\Ontario_Dam_Inventory\Ontario_Dam_Inventory.shp"
hydro_rivers_path = r"M:\School\4YP3\DS\Data\HydroRIVERS_v10_shp\HydroRIVERS_v10_shp\HydroRIVERS_v10.shp"
geodar_dams_path = r"M:\School\4YP3\DS\Data\GeoDAR_v10_v11\GeoDAR_v10_v11\GeoDAR_v11_dams.shp"
geodar_res_path = r"M:\School\4YP3\DS\Data\GeoDAR_v10_v11\GeoDAR_v10_v11\GeoDAR_v11_reservoirs.shp"
basin_clip_path = r"M:\School\4YP3\DS\Data\Proper_Ottawa_Basin.geojson"
out_path = r"M:\School\4YP3\DS\Data\clipped_dams.shp"
out_pathb = r"M:\School\4YP3\DS\Data\buffed_.shp"

#clip to match regional basin
clipped_dams_on = clipping(on_dam_path,basin_clip_path)
clipped_hydro_rivers = clipping(hydro_rivers_path,basin_clip_path)
clipped_geodar_dams = clipping(geodar_dams_path,basin_clip_path)
clipped_geodar_res = clipping(geodar_res_path,basin_clip_path)
#QgsProject.instance().addMapLayer(clipped_dams_on['OUTPUT'])
#QgsProject.instance().addMapLayer(clipped_hydro_rivers['OUTPUT'])
#QgsProject.instance().addMapLayer(clipped_geodar_dams['OUTPUT'])
#QgsProject.instance().addMapLayer(clipped_geodar_res['OUTPUT'])


#reproject layers to match regional CRS
repro_dams_on = reproject_crs(clipped_dams_on['OUTPUT'],'EPSG:32618')
repro_hydro_rivers = reproject_crs(clipped_hydro_rivers['OUTPUT'],'EPSG:32618')
repro_geodar_dam = reproject_crs(clipped_geodar_dams['OUTPUT'],'EPSG:32618')
repro_geodar_res = reproject_crs(clipped_geodar_res['OUTPUT'],'EPSG:32618')
#add layer to map for visual verify
QgsProject.instance().addMapLayer(repro_dams_on['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_hydro_rivers['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_geodar_dam['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_geodar_res['OUTPUT'])

#buffer geodar dams 
buff_geodar_dams = buff_points(2000,repro_geodar_dam['OUTPUT'])
QgsProject.instance().addMapLayer(buff_geodar_dams['OUTPUT'])
#location query
processing.run('qgis:selectbylocation',
    {'INPUT': repro_dams_on['OUTPUT'],
    'PREDICATE': [6],
    'INTERSECT': buff_geodar_dams['OUTPUT'],
    'METHOD':0}
    )
#delete duplicates 
repro_dams_on['OUTPUT'].startEditing()
repro_dams_on['OUTPUT'].deleteSelectedFeatures()
repro_dams_on['OUTPUT'].commitChanges()
print("%s seconds" % (time.time() - start_time))