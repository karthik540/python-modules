import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret , frame = cap.read()
    #   RGB -> Grey Conversion (Optional)
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Grey SelfCam' , gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 