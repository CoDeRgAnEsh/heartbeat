import sys
import video
import processing

__version__ = 0.1

def main(): 
    print("Heartbeat v{}".format(__version__))
    if(len(sys.argv) < 2):
        print("Usage: '{} <path to video>'".format(sys.argv[0]))
        return 

    processing.process_video(sys.argv[1])

if __name__ == '__main__':
    main()
