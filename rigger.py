import bpy



context = bpy.context
objects = bpy.data.objects
data = bpy.data
selector = bpy.ops.object
ARMATURE_NAME = 'Armature.001'

def init_objects(armature_name,coll_name):
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


def make_parent(ARMATURE_NAME):
    armature, other_objects = init_objects()
    select_arma(arma=armature,others=other_objects)
    
