from flask import Flask, render_template, Response
from processor.simple_streamer import SimpleStreamer as VideoCamera
from processor.face_detector import FaceDetector as VideoCamera

import time
import threading
import baby
import numpy

print("1>>>>>>>>>>>>>>>>>>>>>>>>>")
video_camera = VideoCamera(flip=False)
print("2>>>>>>>>>>>>>>>>>>>>>>>>>")
app = Flask(__name__)
print("3>>>>>>>>>>>>>>>>>>>>>>>>>")
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def entry():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>app")
    app.run(host='0.0.0.0', debug=False, threaded=True)

print(">>>>>>>>>entry before")
entry()