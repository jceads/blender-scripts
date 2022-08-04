from file_size_reducer import optimezeFiles
from pygltflib import GLTF2
from pygltflib.utils import ImageFormat,glb2gltf,gltf2glb
import os

#!GLB DOSYASI İLE AYNI KLASÖRDE OLMASI GEREKİYOR

glb_file = None
for file in os.listdir():
    if ".glb" in file:
        glb_file = file
        break

gltf = GLTF2().load(glb_file)
for image in range(0,len(gltf.images)):
    gltf.export_image_to_file(image_index=image)#GLB DOSYASINDAKİ PNG DOSYALARINI ÇIKARIR

optimezeFiles()#ÇIKARILAN PNG LERİ OPTİMİZE EDER
glb2gltf(glb_file)
gltf2glb(source=glb_file,destination="optimized.glb")#OPTİMİZE EDİLMİŞ HALDE TEKRAR GLB FORMATINA DÖNÜŞTÜRÜR !! TODO: OPTİMİZE EDİLMEMİŞ PNGLERİ KULLANMASINI DÜZELTME
