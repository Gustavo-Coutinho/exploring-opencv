import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 1)
cap.set(4, 1)
while True:
    #capture frame-by-frame
    ret, frame = cap.read()
    #convert color to grayscale for windows named 'gray' 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray      
    #make it possible to break out of application by pressing 'q'
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
#when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()