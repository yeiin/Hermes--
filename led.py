import RPi.GPIO as GPIO
import time
import random

print(">>>>>>>>>>>>>>>>>>>>>>>>led")

GPIO.setmode(GPIO.BCM)

LED1 = 21 # BCM P21
LED2 = 20

light_list = [LED1, LED2]

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# pwm = GPIO.PWM(12,50) #50hz  
# pwm.start(0)  

dc = 0

print(">>>>>>>>>>>>>>>>>>>>>>>>led")


def lightOn(light):
    dc = 100
    GPIO.output(light, GPIO.HIGH)


def lightOff(light):
    dc = 0
    GPIO.output(light, GPIO.LOW)


def lighting():
     
    while 1:                        # 무한 반복 - LED On/Off
        
        light = random.choice(light_list)
        
        GPIO.output(light, GPIO.HIGH) 
        dc = 100
        time.sleep(0.5)

        GPIO.output(light, GPIO.LOW)
        dc = 0
        time.sleep(0.5)
        

# def changDutyCycle(mode):
#     if(mode == 0):   
#         dc -= 5
#         pwm.ChangeDutyCycle(dc)
#     else:
#         dc += 5
#         pwm.ChangeDutyCycle(dc)