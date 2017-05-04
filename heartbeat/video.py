import cv2
import numpy as np

def calculate_brightness(video_path):

    print("Opening", video_path);

    #Get video
    video = cv2.VideoCapture(video_path)    

    #Check video was opened
    if(not video.isOpened()):
        raise FileNotFoundError("Failed to open '{}'".format(video_path))

    #Get video FPS
    FPS = video.get(cv2.CAP_PROP_FPS)       
    #Set brightness empty initially
    brightness = []                         

    #Calculate progress
    progress = 10
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    count = 0

    print("Processed {}% of {}".format((10-progress)*10, video_path))
    while(video.isOpened()):
        #Get video frame
        ret, frame = video.read()           

        #Print progress
        count += 1
        if(count*progress > frames):
            progress -= 1
            print("Processed {}% of {}".format((10-progress)*10, video_path))

        #Check is there is a frame
        if ret is False:                    
            break
        
        #Get mean of red channel as brightness
        brightness.append(np.mean(frame[:,:,2]))
       
    print("Closing", video_path)
    #Release video
    video.release()

    return brightness, FPS

