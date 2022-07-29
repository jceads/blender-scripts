import os
from urllib.request import install_opener
import blender



import subprocess
import bpy
import os

blender_dir = "C:/users/jcead/desktop/blender"


def select_all_glb_models():
    glb_container =[]
    for glb_model in os.listdir():
        glb_container.append(glb_model)
    return glb_container

def import_and_export_models(gltf_model_container):
    for model in gltf_model_container:
        bpy.ops.import_scene.gltf(files=model)
        bpy.ops.export_scene.gltf(filepath="/"+model.name,export_texture_dir="/"+model.name+"/textures")#maybe need delete previous model before export




command_list =[
    blender_dir,
    "--background"
]

subprocess.run(blender_dir)









files_will_import = select_all_glb_models()
print(files_will_import)
# import each model to blender
# bpy.ops.import_scene.gltf()
# export each model with gltf option
