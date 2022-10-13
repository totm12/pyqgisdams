import processing

def clipping(lyr1, lyr2, lyr3):
    #Run clip tool.
    #Parameters:
    #lyr1 : shapefile//path
    #The name of the input shapefile to be clipped
    #lyr2 : path to vector data
    #The name of the overlay area
    #lyr3 : shapefile//path
    #The name of the output path
    layer_clip = processing.run('qgis:clip',
        {'INPUT': lyr1,
        'OVERLAY': lyr2,
        'OUTPUT': lyr3}
    )
    return lyr3

def buff_points(static_dis, lyr, lyr2):
    #Run buffer tool on clipped points.
    #Parameters:
    #static_dis : shapefile//path
    #The value used to buffer by (distance)
    #lyr : shapefile//path
    #The name of the input shapefile to buffer
    #lyr2 : shapefile//path
    #The name of the output path
    processing.run('native:buffer',
        {'INPUT': lyr,
        'DISTANCE':static_dis,
        'OUTPUT': lyr2}
    )
    return lyr2

#Set input and output file paths
in_path = r"M:\School\4YP3\DS\Data\Ontario_Dam_Inventory\Ontario_Dam_Inventory.shp"
clip_path = r"M:\School\4YP3\DS\Data\basin_ottawa.geojson"
out_path = r"M:\School\4YP3\DS\Data\clipped_dams.shp"
out_pathb = r"M:\School\4YP3\DS\Data\buffed_.shp"
clipped_dams = clipping(in_path,clip_path,out_path)

#Add clipped layer to QGIS interface
iface.addVectorLayer(clipped_dams,'', 'ogr')
buffd_dams = buff_points(2,clipped_dams,r"M:\School\4YP3\DS\Data\buffdams.shp") 
iface.addVectorLayer(buffd_dams,'', 'ogr')
