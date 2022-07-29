import imp
import json
import bpy
import os
# import rigger as rg
#exclude = false //açar


def export_model(obj_name):
    armature_name = 'Armature.001'
    # bpy.ops.object.select_all()
    # bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
    make_parent(ARMATURE_NAME=armature_name,collection_name='rig_placement')
    print(f"exporting {obj_name}")
    filepath = f"C:/Users/jcead/desktop/BMNFT_output/{obj_name}.glb"
    bpy.ops.export_scene.gltf(filepath=filepath,export_format = "GLB",ui_tab = "MESHES",use_visible=True)
    print("exported")
    bpy.ops.object.select_all()
    hide_and_clear_parent(target_will_hide=armature_name)

def hide_and_clear_parent(target_will_hide):
    target_armature = 'target_will_hide'
    bpy.data.objects[target_armature].hide_viewport = True
    bpy.ops.object.select_all()
    bpy.ops.object.parent_clear(type='CLEAR')


def closeAllCollection():
    layers = bpy.context.layer_collection.children
    for coll in layers:
        coll.exclude = True
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

# get_all_variants() closed for test purpose

export_model('test_object')


#RIGGER.PY FILE

context = bpy.context
objects = bpy.data.objects
data = bpy.data
selector = bpy.ops.object
ARMATURE_NAME = 'Armature.001'

def init_objects(armature_name,coll_name = 'rig_placement'):
    other_objects= []
    #searching armature and other objects collection. Will be in script_ignore
    for item in data.collections[coll_name].all_objects:
            other_objects.append(item)
    print('all objects initialized')
    return bpy.data.objects[armature_name], other_objects

def set_parent():
    print('parenting to bone')
    selector.parent_set(type='ARMATURE_AUTO',keep_transform=True)
    

def select_arma(arma,others):
    for item in others:
        item.select_set(True)
    
    arma.select_set(True)
    set_parent()


def make_parent(ARMATURE_NAME,collection_name):
    armature, other_objects = init_objects(ARMATURE_NAME,coll_name=collection_name)
    select_arma(arma=armature,others=other_objects)
    
