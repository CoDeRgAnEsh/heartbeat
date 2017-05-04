import sys
import video
import processing

def main(): 
    if(len(sys.argv) < 2):
        print("Usage: '{} <path to video>'".format(sys.argv[0]))
        return 

    processing.process_video(sys.argv[1])

if __name__ == '__main__':
    main()
