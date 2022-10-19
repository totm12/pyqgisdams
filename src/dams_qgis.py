import processing
import time

def reproject_crs(lyr1, change_crs):
    #Returns reprojected geometry.
    #Parameters:
    #lyr1 : shapefile//path
    #The name/path of the layer to be reprojected
    #change_crs : string of the new CRS
    #(Uses temp layers to reduce memory consumption)
    #print(lyr1,change_crs)
    rp = processing.run('native:reprojectlayer',
    {'INPUT': lyr1,
    'TARGET_CRS': change_crs,
    'OUTPUT': 'memory:Reprojected'}
    )
    return rp

def clipping(lyr1, lyr2):
    #Returns geometry clipped to overlay.
    #Parameters:
    #lyr1 : shapefile//path
    #The name of the input shapefile to be clipped
    #lyr2 : path to vector data
    #The name of the overlay area to clip against
    layer_clip = processing.run('qgis:clip',
        {'INPUT': lyr1,
        'OVERLAY': lyr2,
        'OUTPUT': 'memory:Clipped'}
    )
    return layer_clip

def buff_points(static_dis, lyr):
    #Returns buffered point geometry.
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

def query_count(lyr1, lyr2):
    #Returns count of selected features within and
    #updated layer with duplicates deleted.
    #Parameters:
    #static_dis : shapefile//path
    #The value used to buffer by (distance)
    #lyr : shapefile//path
    #The name of the input shapefile to buffer
    #lyr2 : shapefile//path
    #The name of the output path
    local_s = processing.run('qgis:selectbylocation',
    {'INPUT': lyr1,
    'PREDICATE': [6],
    'INTERSECT': lyr2,
    'METHOD':0}
    )
    s_feature = lyr1.selectedFeatureCount()
    lyr1.startEditing()
    lyr1.deleteSelectedFeatures()
    lyr1.deleteAttributes([9])
    lyr1.commitChanges()
    return s_feature, lyr1

def layer_merge(lyr_list):
    #Returns merged vector geometry from list.
    #Parameters:
    #lyr_list : []
    #List of layers to be merged
    merge_on = processing.run('native:mergevectorlayers',
    {'LAYERS': lyr_list,
    'OUTPUT':'memory:Deduplipcated' }
    )
    return merge_on
    
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
#QgsProject.instance().addMapLayer(repro_dams_on['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_hydro_rivers['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_geodar_dam['OUTPUT'])
#QgsProject.instance().addMapLayer(repro_geodar_res['OUTPUT'])

#buffer geodar dams 
buff_geodar_dams = buff_points(2000,repro_geodar_dam['OUTPUT'])
QgsProject.instance().addMapLayer(buff_geodar_dams['OUTPUT'])
QgsProject.instance().addMapLayer(repro_dams_on['OUTPUT'])

#location query
on_count,repro_dams_on['OUTPUT'] = query_count(repro_dams_on['OUTPUT'],buff_geodar_dams['OUTPUT'])

#merge old with new
shapefile_list = [repro_dams_on['OUTPUT'],repro_geodar_dam['OUTPUT']]
merged_data = layer_merge(shapefile_list)
QgsProject.instance().addMapLayer(merged_data['OUTPUT'])
print('Count:',on_count,'duplicate features within a 2km buffer.')
print("%s seconds" % (time.time() - start_time))
