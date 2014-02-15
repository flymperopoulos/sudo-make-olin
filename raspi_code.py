import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
print face_cascade.empty()
cap = cv2.VideoCapture(0)

def detectFaces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces
    morefaces = face_profile_cascade.detectMultiScale(gray, 1.3, 5)
    np.append(faces,morefaces)
    print faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    return frame

def cleanup():
    cv2.destroyAllWindows()
    cap.release()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    result = detectFaces(frame)
    #result = frame

    # Display the resulting frame
    cv2.imshow('frame',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cleanup()
        break
