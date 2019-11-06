import RPi.GPIO as GPIO
import time
import subprocess

def indicate7seg(num,sec):
    
    left   = [3,14]
    center = [4,2,15]
    right  = [17,18]
    
    num = int(num)
    if num < 0:
        print("underflow")
        return -1;
    if num > 9:
        print("overflow")
        return -2;
    
    light_area = [
        [right[0],right[1], center[0],center[2],left[0],left[1]],
        [right[0],right[1]],
        [right[0],center[0],center[1],center[2],left[1]],
        [right[0],right[1], center[0],center[1],center[2]],
        [right[0],right[1], center[1],left[0]],
        [right[1],center[0],center[1],center[2],left[0]],
        [right[1],center[0],center[1],center[2],left[0],left[1]],
        [right[0],right[1], center[0],left[0]],
        [right[0],right[1], center[0],center[1],center[2],left[0],left[1]],
        [right[0],right[1], center[0],center[1],center[2],left[0]],
        ]

    GPIO.setmode(GPIO.BCM)
    
    for i in light_area[num]:
      GPIO.setup(i, GPIO.OUT)
      GPIO.output(i, GPIO.LOW)
    
    time.sleep(sec)
        
    GPIO.cleanup() 
    
