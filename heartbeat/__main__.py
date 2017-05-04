import sys
import video
import processing

def main(): 
    if(len(sys.argv) < 2):
        print("Usage: '{} <path to video>'".format(sys.argv[0]))
        return 

    brightness, FPS = video.calculate_brightness(sys.argv[1])
    filtered_brightness = processing.filter_brightness(brightness, FPS)
    i = processing.brightness_FFT(filtered_brightness[0:int(6*FPS)])
    print(i)

if __name__ == '__main__':
    main()
