import cv2
import numpy as np
#import simplejson as json
import json
import requests
import Queue
from threading import Thread
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
print face_cascade.empty()
cap = cv2.VideoCapture(0)

frameQueue = Queue.Queue(1000)

def detectFaces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)
    morefaces = face_profile_cascade.detectMultiScale(gray, 1.3, 2)
    np.append(faces,morefaces)
    return faces

def transmitFrame():
    url = 'http://0.0.0.0:5000/upload'
    while True:
        if not frameQueue.empty():
            print "Transmitting!"
            frame = frameQueue.get()
            #payload = {'img':base64.b64encode(json.dumps(frame.tolist()))}
            payload = {'img':json.dumps(frame.tolist())}
            #header = headers = {'Content-type': 'binary/octet-stream','Content-length':len(payload),'Content-transfer-encoding': 'binary',}
            r = requests.post(url,data=payload)

def cleanup():
    cv2.destroyAllWindows()
    cap.release()

postThread = Thread(target=transmitFrame)
postThread.daemon = True
postThread.start()

postThread2 = Thread(target=transmitFrame)
postThread2.daemon = True
postThread2.start()

while(True):
    # Capture frame-by-frame
    time.sleep(.1) # only capture at 10 Hz
    ret, frame = cap.read()

    # Our operations on the frame come here
    face_coords = detectFaces(frame)

    for (x,y,w,h) in face_coords:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = frame[y:y+h, x:x+w]

    if len(face_coords) > 0:
        frameQueue.put(frame)
        #transmitFrame(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cleanup()
        break
