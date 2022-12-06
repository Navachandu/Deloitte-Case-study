import RPi.GPIO as GPIO
import time
import numpy as np
from statistics import mean

print('starting the program')

input_pin=22
timing=[]
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)
i=0
while i<5:
        
        print('inside while loop')
        GPIO.wait_for_edge(input_pin,GPIO.RISING)
        risingtime= time.time()
        #print(time.time())
        #print('daf')       
        GPIO.wait_for_edge(input_pin,GPIO.FALLING)
        #print( time.time())

        fallingtime= time.time()
        dutycycletime=fallingtime-risingtime
        if dutycycletime <=0.001:
            timing.append(dutycycletime)
            i=i+1
        #print(fallingtime-risingtime)
        
'''        
        GPIO.wait_for_edge(input_pin,GPIO.RISING)
        risingtime1= time.time()
        #print(' total falling time'+ risingtime1-fallingtime)

        
'''
print(timing)
print('average')
print(mean(timing))

avg=mean(timing)
percent=(avg)*100000
print(percent)


