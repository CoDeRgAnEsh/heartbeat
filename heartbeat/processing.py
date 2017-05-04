from scipy import signal
from numpy import fft
import scipy.fftpack
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

def FFT(brightness, inc = 1):
    fft_amp = abs(fft.fft(brightness, inc*brightness.shape[0]))
    return fft_amp[0:fft_amp.shape[0]//2]

def find_peak(array):
    m = 0
    for i in range(array.shape[0]):
        if(array[i] > array[m]):
            m=i
    return m

