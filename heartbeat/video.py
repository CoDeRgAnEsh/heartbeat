import cv2
import numpy as np

def calculate_brightness(video_path):
    #Get video
    video = cv2.VideoCapture(video_path)    
    #Get video FPS
    FPS = video.get(cv2.CAP_PROP_FPS)       
    #Set brightness empty initially
    brightness = []                         

    while(video.isOpened()):
        #Get video frame
        ret, frame = video.read()           

        #Check is there is a frame
        if ret is False:                    
            break
        
        #Get mean of red channel as brightness
        brightness.append(np.mean(frame[:,:,2])
       
    #Release video
    video.release()

    return brightness, FPS

