from scipy import signal
import numpy as np
import video
import matplotlib.pyplot as plt

def filter_brightness(brightness, FPS):
    BPM_L = 40
    BPM_H = 230
    FILTER_STABILIZATION_TIME = 1
    b, a = signal.butter(2, [(BPM_L/60)/FPS*2, (BPM_H/60)/FPS*2], 'bandpass')
    filtered = signal.lfilter(b,a,brightness)
    filtered = filtered[int(FPS*FILTER_STABILIZATION_TIME+1):filtered.size]
    return filtered

if __name__=='__main__':
    brightness, FPS = video.calculate_brightness('data/video.mp4')
    filtered_brightness = filter_brightness(brightness, FPS)
    plt.plot(filtered_brightness)
    plt.show()
    
