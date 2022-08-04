import json
import bpy
import os



def export_model(obj_name):
    so = bpy.context.selected_objects
    if len(so) == 0:
        bpy.ops.object.select_all()
    print(f"exporting {obj_name}")
    filepath = f"C:/Users/jcead/desktop/BMNFT_output/{obj_name}.glb"#export edilecek klasörün var olması gerekiyor
    bpy.ops.export_scene.gltf(filepath=filepath, export_format = "GLB",
                              ui_tab = "MESHES",
                              use_visible=True,
                              export_draco_mesh_compression_enable=True,
                              )
    print(f"exported{obj_name}")


def closeAllCollection():
    layers = bpy.context.layer_collection.children
    for index in range(1,len(layers)):
        layers[index].exclude = True
    print("all collections closed")


def open_selected_and_export_coll(json_ref):
    collections = bpy.context.layer_collection.children
    values = json_ref["NFT_Variants"].values()
    for sub_coll in range(1,len(collections)):#ignores firs collection which is 'Script Ignore'
        for i in range(0,len(collections[sub_coll].children)):
            for value_key in values:
                if value_key == collections[sub_coll].children[i].name:
                    collections[sub_coll].children[i].exclude = False #This object will be visible
    export_model(json_ref["name"])#uses for only naming
    print("model exported")

def getJsonFiles():
    #generate edilecek json dosyalarının dosya yolu girilmelidir
    desktop_dir = "C:/Users/jcead/desktop/lidy/Blend_My_NFTs Output/Generated NFT Batches/Batch1/BMNFT_metaData/"
    temp = [pos_json for pos_json in os.listdir(desktop_dir) if pos_json.endswith(".json")]
    print("***********************")
    
    json_obj_list = []
    for i in temp:
        print("i: ", i)
        json_obj_list.append(json.load(open(desktop_dir+i)))
    print("json files: ", json_obj_list)
    print("*************************")
    return json_obj_list

def get_all_variants():
    """This is where generating starts"""
    print('Starting')
    json_obj_list = getJsonFiles()
    print('json file used')
    for index in range(0,len(json_obj_list)):
        closeAllCollection()
        print('all collections closed')
        open_selected_and_export_coll(json_obj_list[index])
        print('selected exported')
        

get_all_variants()