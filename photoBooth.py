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

def sayCheese():
    with picamera.PiCamera() as camera:
<<<<<<< HEAD
        camera.resolution = (800,600)
=======
    	#will need to change this after testing 
    	#different picture sizes
    
        camera.resolution = (1024,768)
>>>>>>> 4166cd78baba7ab4f6f92b19a53824ac1358e4fe
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
    

