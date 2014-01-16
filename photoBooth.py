#!/usr/bin/python
import time 
import picamera
import RPi.GPIO as GPIO
import subprocess

#GPIO Pin on Adafruit breakout board
pushBtn = 23
#directory where camera images will be stored
imgPath = './images/'
#piCamera initialization calls
camera = picamera.PiCamera()
camera.resolution = (1280,960)
camera.start_preview()
#GPIO setup calls
GPIO.setmode(GPIO.BCM)
GPIO.setup(pushBtn, GPIO.IN)

#placeholder for print 
def printPix():
    global imgPath
    Proc = subprocess.Popen(['lpr', imgPath +'montage.jpg'])

#call montage from ImageMagick package
def createPixStrip():
    global imgPath
    Proc = subprocess.Popen(['montage', imgPath + 'pic0.jpg', imgPath + 'pic1.jpg', 
        imgPath +'pic2.jpg', '-mode', 'Concatenate', '-tile', '1x3', imgPath + 'montage.jpg' + str(time.time())]) 

#call our 3,2,1 countdown blob
def countDown():
    Proc = subprocess.Popen('./hello_font.bin')

def sayCheese():
    global imgPath
    global camera
    for i in range(0,3):
        countDown() 
        time.sleep(3)
        photoFile =  '%spic%s.jpg' %(imgPath, i)
        print "Take Picture " + str(i)  
        camera.capture(photoFile)

def buttonMon():
    if ( GPIO.input(pushBtn) == False ):
        print "Button Pressed...Taking Picture"
        sayCheese()
        createPixStrip()  
    else:
        print "Button Open"

    time.sleep(1.0);

while True:
   buttonMon(); 
    

