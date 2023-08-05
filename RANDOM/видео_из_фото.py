'''
Purpose: Видео из коллекции снимков
'''
import cv2
import numpy as np
import glob
import time

# формат даты для названия видео
timestr = time.strftime("%y%m%d %H%M%S")
# выходной формат
frameSize = (1280, 720)
# куда сохраняем видео
out = cv2.VideoWriter(f'C:/Users/warning/Downloads/{timestr}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, frameSize)
# откуда берем снимки
for filename in glob.glob('C:/Users/warning/Pictures/Camera Roll/*.jpg'):
    img = cv2.imread(filename)
    out.write(img)
# завершить видео
out.release()