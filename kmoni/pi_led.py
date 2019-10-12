import RPi.GPIO as GPIO
import time
import subprocess

def flash(GPIOpin,cnt,loop_cnt=1):
    for i in range(loop_cnt):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIOpin, GPIO.OUT)
        
        for i in range(cnt):
            GPIO.output(GPIOpin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(GPIOpin, GPIO.LOW)
            time.sleep(0.05)
        
        time.sleep(2-(cnt*0.2))

    GPIO.cleanup() # <- 消灯
    