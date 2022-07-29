from file_size_reducer import optimezeFiles
from pygltflib import GLTF2
from pygltflib.utils import ImageFormat,glb2gltf,gltf2glb
import os

glb_file = None

for file in os.listdir():
    if ".glb" in file:
        glb_file = file
        break

gltf = GLTF2().load(glb_file)
for image in range(0,len(gltf.images)):
    gltf.export_image_to_file(image_index=image)

optimezeFiles()
glb2gltf(glb_file)
gltf2glb(source=glb_file,destination="optimized.glb")
# gltf.images[0].uri = str(glb_file)[::-3]+"_image"  # will save the data uri to this file (regardless of data format)
# gltf.convert_images(ImageFormat.FILE)
