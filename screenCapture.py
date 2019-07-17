from PIL import ImageGrab
import cv2 , time
import numpy as np

while(True):
    last_time = time.time()
    image = np.array(ImageGrab.grab(bbox= (0,30,700,450)))

    cv2.imshow('window' , cv2.cvtColor(image , cv2.COLOR_BGR2RGB))

    print("FPS: {}".format(1/(time.time() - last_time)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

