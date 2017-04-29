from scipy import signal
import numpy as np
import video
import matplotlib.pyplot as plt

def filter_brightness(brightness, FPS):
    #Set low and high BPM limits
    BPM_L = 40
    BPM_H = 230
    #Set filter stabilization time in seconds
    FILTER_STABILIZATION_TIME = 1
    #Create a digital butterworth filter (frequencies are normalized, 1 corresponds to half the sampling rate)
    b, a = signal.butter(2, [(BPM_L/60)/FPS*2, (BPM_H/60)/FPS*2], 'bandpass')
    #Apply filter
    filtered = signal.lfilter(b,a,brightness)
    #Remove initial stabilization time
    filtered = filtered[int(FPS*FILTER_STABILIZATION_TIME+1):filtered.size]

    return filtered

if __name__=='__main__':
    brightness, FPS = video.calculate_brightness('data/video.mp4')
    filtered_brightness = filter_brightness(brightness, FPS)
    plt.plot(filtered_brightness)
    plt.show()
    
