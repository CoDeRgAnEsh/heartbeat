import cv2
import numpy as np
import os

def calculate_brightness(video_path):
    video = cv2.VideoCapture(video_path)
    FPS = video.get(cv2.CAP_PROP_FPS)
    brightness = []

    while(video.isOpened()):
        ret, frame = video.read()

        if ret is False:
            break

        brightness.append(np.mean(frame[:,:,2]))
       
    video.release()
    cv2.destroyAllWindows()

    return brightness, FPS

