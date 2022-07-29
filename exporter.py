import imp
import json
import bpy
import os
import rigger as rg
#exclude = false //açar


def export_model(obj_name):
    bpy.ops.object.select_all()
    bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
    make_parent()
    print(f"exporting {obj_name}")
    filepath = f"C:/Users/jcead/desktop/BMNFT_output/{obj_name}.glb"
    bpy.ops.export_scene.gltf(filepath=filepath,export_format = "GLB",ui_tab = "MESHES",use_visible=True)
    print("exported")
    bpy.ops.object.select_all()
    hide_and_clear_parent()

def hide_and_clear_parent():
    target_armature = 'test-rig'
    bpy.data.objects[target_armature].hide_viewport = True
    bpy.ops.object.select_all()
    bpy.ops.object.parent_clear(type='CLEAR')

def make_parent():
    rg.make_parent()

def closeAllCollection():
    layers = bpy.context.layer_collection.children
    collections = layers
    for coll in collections:
        coll.exclude = True
    print("all collections closed")


# close all open once
def open_selected_and_export_coll(json_ref):
    collections = bpy.context.layer_collection.children
    values = json_ref["NFT_Variants"].values()
    for sub_coll in range(1,len(collections)):
        for i in range(0,len(collections[sub_coll].children)):
            for value_key in values:
                if value_key == collections[sub_coll].children[i].name:
                    collections[sub_coll].children[i].exclude = False
    export_model(json_ref["name"])
    print("model exported")

def getJsonFiles():
    print("listdir: ",)
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
    json_obj_list = getJsonFiles()
    for index in range(0,len(json_obj_list)):
        closeAllCollection()
        open_selected_and_export_coll(json_obj_list[index])

get_all_variants()
