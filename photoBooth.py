#!/usr/bin/python
import time 
import picamera
import RPi.GPIO as GPIO
import subprocess

#using the GPIO 23 pin as marked on the 
#adafruit breakout board
pushBtn = 23
imgPath = './images/'

GPIO.setmode(GPIO.BCM)
GPIO.setup(pushBtn, GPIO.IN)

def createPixStrip():
    global imgPath
    Proc = subprocess.Popen(['montage', './images/pic0.jpg', './images/pic1.jpg', './images/pic2.jpg', '-mode', 'Concatenate', '-tile', '1x3', './images/montage.jpg'])

def sayCheese():
    with picamera.PiCamera() as camera:
        camera.resolution = (800,600)
	global imgPath
        for i in range(0,3):
            camera.start_preview()
            # camera needs to "warm up"
            time.sleep(4)
            photoFile = imgPath + 'pic' + str(i) + '.jpg'
            print "Take Picture " + str(i)  
	    camera.capture(photoFile)


while True:
    if ( GPIO.input(pushBtn) == False ):
        print "Button Pressed\n Taking Picture"
        sayCheese()
        createPixStrip()  
    else:
        print "Button Open"

    time.sleep(1.0);
    

