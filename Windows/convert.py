import os
import time
from subprocess import call
from shutil import move

videos = []

current_dir = os.path.dirname(os.path.realpath(__file__))
processed_dir = os.path.realpath(current_dir + "/processed")

for file in os.listdir(current_dir):
    if file.endswith(".MTS"):
        videos.append(file)

for vidja in videos:
    arguments = 'ffmpeg/bin/ffmpeg -i {} -c:v copy -c:a pcm_s16le converted/{}.mov'.format(vidja,vidja.split('.')[0])
    call(arguments, shell=False)
    move(os.path.realpath(vidja), processed_dir)
    

time.sleep(10)