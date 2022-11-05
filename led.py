import RPi.GPIO as GPIO
import time
import random
import constant
import baby

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED1 = 21 # BCM P21
LED2 = 20

light_list = [LED1, LED2]

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

pwm1 = GPIO.PWM(21,50) #50hz  
pwm2 = GPIO.PWM(20,50) #50hz  
pwm1.start(0)  
pwm2.start(0)  

dc = 0

    

def lightOn(light):
    global dc
    dc = 100
    GPIO.output(light, GPIO.HIGH)


def lightOff(light):
    global dc
    dc = 0
    GPIO.output(light, GPIO.LOW)


def lighting():
    global dc
    print(">>>>>>>>>>>lighting")
    while 1:                        # 무한 반복 - LED On/Off
        
        light = random.choice(light_list)
        
        GPIO.output(light, GPIO.HIGH) 
        dc = 100
        time.sleep(0.5)

        GPIO.output(light, GPIO.LOW)
        dc = 0
        time.sleep(0.5)
        

def changDutyCycle(mode):
    global dc
    if(mode == 0):   
        dc -= 5
        pwm1.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        print(dc)
    else:
        dc += 5
        pwm1.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        print(dc)

def main():
    baby.baby = constant.SLEEPTOWAKE
    if(baby.baby == constant.SLEEPTOWAKE):
        # lighting()
        lightOn(LED1)
        print(dc)
        while(1):
            while(dc>=5):
                changDutyCycle(0)
                time.sleep(1)
            while(dc<=95):
                changDutyCycle(1)
                time.sleep(1)
    

if __name__ == "__main__":
    main()