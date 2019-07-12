import urllib.request
import cv2
import numpy as np
import time

url = "http://192.168.43.1:8080/shot.jpg?rnd=916450"

while(True):
    last_time = time.time()
    resp = urllib.request.urlopen(url)
    imgNp = np.asarray(bytearray(resp.read()) , dtype=np.uint8)
    img = cv2.imdecode(imgNp , -1)
    cv2.imshow('test' , img)
    print('FPS: {}'.format(1/(time.time() - last_time)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
