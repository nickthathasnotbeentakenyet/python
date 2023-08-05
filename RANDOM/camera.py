'''
Purpose: Запись с камеры в покадровое видео
# FIXME: Неверная раскадровка
'''
import cv2
import time
import numpy as np

# сутки = 86 400
# время записи в секундах
DURATION = 15
# частота кадров
FRAMES_PER_SECOND = 30.0
# # количество снимков за запись
# RATE = DURATION / FRAMES_PER_SECOND
# видео устройство
CAMERA = cv2.VideoCapture(0)
# разрешение видео
FRAME_SIZE = (640, 480)
# выходной формат
VIDEO_FORMAT = cv2.VideoWriter_fourcc(*"XVID")
# путь к конечному файлу записи
PATH = 'C:\\Users\\warning\\Downloads\\'
# проверяем, если камера включена и доступна
if CAMERA.isOpened() is not False:
    # создаем запись
    record = cv2.VideoWriter(f"{PATH}{time.strftime('%Y-%m-%d_%H%M%S')}.avi", VIDEO_FORMAT, FRAMES_PER_SECOND, FRAME_SIZE)
    # пишем в запись
    for i in range(0, int(DURATION * FRAMES_PER_SECOND)):
        ret, frame = CAMERA.read()
        record.write(frame)
    record.release()