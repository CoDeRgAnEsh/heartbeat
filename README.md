# Heartbeat
**Heartbeat** is a software to measure heart rate using a camera.

Based on ["Measuring heart rate with a smartphone camera"](http://www.ignaciomellado.es/blog/Measuring-heart-rate-with-a-smartphone-camera).

## Introduction

When the blood flows through the tip of your finger, your finger's opacity varies. If you cover your smartphone's camera with your finger the image turns red. If you watch closely you can notice that the screen 'pulses'. If your screen is too dark try aiming at a light source or turning on the flashlight.

The objective of **Heartbeat** is to measure heart rate using a smartphone camera. It's based on the fact explained in the previous paragraph. It measures the screen's mean brightness and uses Fourier transform to find the frequencies of the oscillation.

## Requirements

* `OpenCV-Python v3.2`
* `Numpy v1.12`
* `SciPy v0.19`
* `Matplotlib v2.0`
* `Python v3.5`

*Versions tested. Probably works with previous versions.*

## How to use

For now, **Heartbeat** has a very simple command-line interface.

### 1) Get source code
    git clone https://github.com/matheuscarius/heartbeat.git
    cd heartbeat
### 2) Run the program
    python3 heartbeat <path to video file>

## Example
There is a sample video inside the `data/` folder
### Run sample video
    python3 heartbeat data/vid.mp4

## Additional information

You may want to downscale your video before running **Heartbeat** to improve performance. High resolutions are not required for **Heartbeat** to work, 320x240 is sufficient.

You can use tools like ffmpeg, mencoder, avconv, VLC Media Player, etc. to downscale a video.

## Screenshots
### Output of sample video
![Sample video output](https://s8.postimg.org/s3bwolytx/Screenshot_from_2017-05-04_22-36-43.png)
