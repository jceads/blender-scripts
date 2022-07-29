from email.mime import image
import subprocess
import os
from PIL import Image



FFMPEG = "C:/ffmpeg/bin/ffmpeg"

def calculateReso(image):
    _image = Image.open(image)
    if _image.width>1024:
        return 1024
    elif _image.width<1024:
        return 512
    

def build_ffmpeg(fileName,resolution = 1024):
    resolution = calculateReso(fileName)
    scale = "scale="+str(resolution)+":"+str(resolution)
    outputFile = "_"+fileName
    commands_list = [
        FFMPEG,
        "-i",
        fileName,
        "-vf",
        scale,
        outputFile
    ]
    return commands_list

def runFFmpeg(commands):

    if subprocess.run(commands).returncode == 0:
        print("files optimized succesfuly")
    else:
        print("there is error from script")


def optimezeFiles():
    images = search_for_images()
    for i in range(0,len(images)):
        runFFmpeg(build_ffmpeg(images[i]))
        os.remove(images[i])
        os.rename("_"+images[i],images[i])


def search_for_images():
    file_list =   []
    for file_name in os.listdir():
        if ".png" in file_name:
            file_list.append(file_name)
    return file_list

def delete_all_images():
    list_of_images = []
    for i in os.listdir():
        if ".png" in i:
            os.remove(i)

optimezeFiles()