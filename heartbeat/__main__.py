import sys
import video
from processing import *

def main(): 
    if(len(sys.argv) < 2):
        print("Usage: '{} <path to video>'".format(sys.argv[0]))
        return 

    brightness, FPS = video.calculate_brightness(sys.argv[1])
    filtered_brightness = filter_brightness(brightness, FPS)
    i = brightness_FFT(filtered_brightness[0:int(6*FPS)])
    print(i)

if __name__ == '__main__':
    main()
