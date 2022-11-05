import threading 
import time
import camera
import baby

def main():
	
	try:
		t1 = threading.Thread(target=baby.main)
		t1.start()
		t2 = threading.Thread(target=camera)
		t2.start()
  
		while True:
			time.sleep(0.1)
	
	except KeyboardInterrupt:
		print("Ctrl+C Pressed.")
		global flag_exit
		flag_exit = True
		
		t1.join()
		t2.join()

		
if __name__ == "__main__":
	main()