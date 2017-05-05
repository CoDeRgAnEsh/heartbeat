from scipy import signal
from numpy import fft
import scipy.fftpack
import numpy as np
import video
import matplotlib.pyplot as plt

def filter_brightness(brightness, FPS):
    print("Filtering brightness")

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

def FFT(brightness, inc = 1):
    #Calculate FFT
    fft_amp = abs(fft.fft(brightness, inc*brightness.shape[0]))
    #Return only positive frequencies
    return fft_amp[0:fft_amp.shape[0]//2]

def find_peak(array):
    #Find index of highest peak
    m = 0
    for i in range(array.shape[0]):
        if(array[i] > array[m]):
            m=i
    return m

def process_brightness(brightness, window, step, inc = 1):
    #Build array of frequencies

    print("Calculating FFT and peaks")

    #Initialize values
    i = 0
    freqs = []

    #Calculate frequencies with a sliding window
    while(i+window <= brightness.shape[0]):
        f = find_peak(FFT(brightness[i:i+window]*signal.hann(window), inc))
        freqs.append(f/inc/window)
        i += step

    #Return a Numpy array
    return np.array(freqs)

def process_video(video_path):
    print("Start processing {}".format(video_path))
    #Get video brightness
    brightness, FPS = video.calculate_brightness(video_path)
    #Filter video brightness
    filtered_brightness = filter_brightness(brightness, FPS)
    #Set window and step sizes
    window = int(6*FPS)
    step = int(.5*FPS)
    #Get frequency array
    freqs = process_brightness(filtered_brightness, window, step, 100)
    #Transform frequency array to BPM
    freqs *= FPS*60
    #Build time array
    t = np.linspace(window/FPS, filtered_brightness.shape[0]/FPS, freqs.shape[0]) 

    print("Plotting heart rate")

    #Plot frequency
    plt.plot(t, freqs)
    plt.xlabel("Time (s)")
    plt.ylabel("Heart rate (BPM)")
    plt.title(video_path)
    plt.show()
   
    
