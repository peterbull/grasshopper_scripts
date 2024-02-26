import rhinoscriptsyntax as rs

def DuplicateLayerWithContents(layer_name):
    new_layer_name = layer_name + "_copy"
    rs.AddLayer(new_layer_name)
    
    sublayers = rs.LayerChildren(layer_name)
    if sublayers:
        for sublayer in sublayers:
            new_sublayer_name = sublayer + "_copy"
            rs.AddLayer(new_sublayer_name, parent=new_layer_name)
            
            objects_in_sublayer = rs.ObjectsByLayer(sublayer)
            if objects_in_sublayer:
                rs.CopyObjects(objects_in_sublayer)
                rs.ObjectLayer(objects_in_sublayer, new_sublayer_name)
    
    objects_in_layer = rs.ObjectsByLayer(layer_name)
    if objects_in_layer:
        rs.CopyObjects(objects_in_layer)
        rs.ObjectLayer(objects_in_layer, new_layer_name)

layer_to_duplicate = "Guess_Base"  # Replace with the layer name you wish to duplicate
DuplicateLayerWithContents(layer_to_duplicate)
