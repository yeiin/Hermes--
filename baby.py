import constant
import threading
import led
import mobile
import audio
import time

baby = None
count = 0

eye_list = [0 for i in range(20)]


def eyeController():
    count0 = eye_list.count(0) #close
    count1 = eye_list.count(1) #open
    count2 = eye_list.count(2) #blink
    
    percentage0 = count0/eye_list.__len__
    percentage1 = count1/eye_list.__len__
    
    
    
    

def main():
    global count
    global baby
    
    baby = constant.SLEEP
    while(1):
        if(baby==constant.AWAKE):
            ledt = threading.Thread(target=led.main)
            mobilet = threading.Thread(target=mobile.main)
            audiot = threading.Thread(target=audio.main)
            ledt.start()
            mobilet.start()
            audiot.start()
            baby=constant.WAKE
        if(baby==constant.NONE):
            ledt.join()
            mobilet.join()
            audiot.join()
        
        if(count == 10):
            baby = constant.NONE
        
        count += 1
        time.sleep(1)
            
            
if __name__ == "__main__":
    main()