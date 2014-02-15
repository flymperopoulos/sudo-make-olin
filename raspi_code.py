import cv2
import numpy as np
import simplejson as json
import requests

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
print face_cascade.empty()
cap = cv2.VideoCapture(0)

def detectFaces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)
    morefaces = face_profile_cascade.detectMultiScale(gray, 1.3, 2)
    np.append(faces,morefaces)
    return faces

def transmitFrame(frame):
    print "Transmitting!"
    url = 'http://0.0.0.0:5000/test'
    r = requests.post(url,data=frame)

def cleanup():
    cv2.destroyAllWindows()
    cap.release()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    face_coords = detectFaces(frame)

    for (x,y,w,h) in face_coords:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = frame[y:y+h, x:x+w]

    if len(face_coords) > 0:
        transmitFrame(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cleanup()
        break
