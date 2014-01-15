#!/usr/bin/python
import time 
import picamera
import RPi.GPIO as GPIO
import subprocess

pushBtn = 23
imgPath = './images/'

camera = picamera.PiCamera()
camera.resolution = (1024,768)
camera.start_preview()


GPIO.setmode(GPIO.BCM)
GPIO.setup(pushBtn, GPIO.IN)

def createPixStrip():
    global imgPath
    Proc = subprocess.Popen(['montage', './images/pic0.jpg', './images/pic1.jpg', './images/pic2.jpg', '-mode', 'Concatenate', '-tile', '1x3', './images/montage.jpg'])

def countDown():
    Proc = subprocess.Popen('./hello_font.bin')

def sayCheese():
    global imgPath
    global camera
    for i in range(0,3):
        countDown() 
        time.sleep(2)
        photoFile = imgPath + 'pic' + str(i) + '.jpg'
        print "Take Picture " + str(i)  
        camera.capture(photoFile)

def buttonMon():
    if ( GPIO.input(pushBtn) == False ):
        print "Button Pressed\n Taking Picture"
        sayCheese()
        createPixStrip()  
    else:
        print "Button Open"

    time.sleep(1.0);

while True:
   buttonMon(); 
   # camera needs to "warm up"
    

