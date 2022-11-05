import threading 
import time
import led
import mobile
import camera

def main():
	
	try:
		t1 = threading.Thread(target=led.main)
		t1.start()
		t2 = threading.Thread(target=mobile.main)
		t2.start()
		t3 = threading.Thread(target=camera)
		t3.start()
  
		while True:
			time.sleep(0.1)
	
	except KeyboardInterrupt:
		print("Ctrl+C Pressed.")
		global flag_exit
		flag_exit = True
		
		t1.join()
		t2.join()
		t3.join()

		
if __name__ == "__main__":
	main()