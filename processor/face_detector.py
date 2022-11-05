from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np
import cv2
import baby

first_read = True

class FaceDetector(object):
    print(">>>>>>>>>>>>>>>>>>>>>>>>1")
    def __init__(self, flip = True):
        print(">>>>>>>>>>>>>>>>>>>>>>>>2")
        self.vs = PiVideoStream(resolution=(800, 608)).start()
        print(">>>>>>>>>>>>>>>>>>>>>>>>10")
        self.flip = flip
        print(">>>>>>>>>>>>>>>>>>>>>>>>20")
        time.sleep(2.0)
        print(">>>>>>>>>>>>>>>>>>>>>>>>30")

        # opencvの顔分類器(CascadeClassifier)をインスタンス化する
        self.face_cascade = cv2.CascadeClassifier('processor/model/haarcascades/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('processor/model/haarcascades/haarcascade_eye.xml')
        print(">>>>>>>>>>>>>>>>>>>>>>>>3")

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame
    

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = self.process_image(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def process_image(self, frame):

        global first_read
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 3)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            face_gray=gray[y:y+h,x:x+w]
            face_color=frame[y:y+h,x:x+w]
        
            eyes = self.eye_cascade.detectMultiScale(face_gray,1.1,3)
        
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                if len(eyes) >= 2:
                    if first_read:
                        cv2.putText(frame, "Eye's detected!", (70, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
                        first_read = False
                        baby.baby = 'DETECTED' 
                    else:
                        cv2.putText(frame, "Eye's Open", (70, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)
                        baby.baby = 'OPENED'
                else:
                    if first_read:
                        cv2.putText(frame, "No Eye's detected", (70, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 2)
                        baby.baby = 'CLOSED'
                    else:
                        cv2.putText(frame, "Blink Detected", (70, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
                        baby.baby = 'BLINKED'

        return frame
