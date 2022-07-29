import bpy



context = bpy.context
objects = bpy.data.objects
data = bpy.data
selector = bpy.ops.object
ARMATURE_NAME = 'Armature.001'
def init_objects():
    other_objects= []
    
    for item in data.collections['test-area'].all_objects:
            other_objects.append(item)
    print('all objects initialized')
    return bpy.data.objects[ARMATURE_NAME], other_objects

def set_parent(parent,child):
    print('parenting to bone')
    selector.parent_set(type='ARMATURE_AUTO',keep_transform=True)
    

def select_arma(arma,others):
    for item in others:
        item.select_set(True)
    
    arma.select_set(True)
    set_parent(arma,others)


def make_parent():
    armature, other_objects = init_objects()
    select_arma(arma=armature,others=other_objects)
    
