import RPi.GPIO as GPIO
import random
import time
import threading
import subprocess


def flash_and_indicate(num,GPIOpin,dur):
    for i in range(1):
        threads = [
            flash_led(num=num,GPIOpin=GPIOpin),
            indicate_7seg(num=num,dur=dur)]
        for thread in threads:
            thread.start()

    for thread in threads:
        thread.join()


class flash_led(threading.Thread):

    def __init__(self,num,GPIOpin):
        self.num = num
        self.GPIOpin = GPIOpin
        threading.Thread.__init__(self)

    def run(self):
        flash(self.GPIOpin,self.num,1,False)


class indicate_7seg(threading.Thread):

    def __init__(self,num,dur):
        self.num = num
        self.dur = dur
        threading.Thread.__init__(self)

    def run(self):
        indicate(self.num,self.dur)


def flash(GPIOpin,cnt,loop_cnt=1,willCleanup=True):
    cnt = int(cnt)
    for i in range(loop_cnt):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIOpin, GPIO.OUT)
        
        for i in range(cnt):
            GPIO.output(GPIOpin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(GPIOpin, GPIO.LOW)
            time.sleep(0.05)
        
        
    if willCleanup:
        time.sleep(2-(cnt*0.2))
        GPIO.cleanup() 
    
def indicate(num,sec,left=-1,center=-1,right=-1):
    
    if left == -1:
        left   = [3,14]
    if center == -1:
        center = [4,2,15]
    if right == -1:
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