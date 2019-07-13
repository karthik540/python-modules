from flask import Flask, render_template
import os
import threading , time
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
webcam_flag = False
def webcamCap():
    while(True):
        global webcam_flag
        ret , frame = cap.read()
        #   RGB -> Grey Conversion (Optional)
        gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Grey SelfCam' , gray_frame)
        global webcam_flag
        print(webcam_flag)
        if webcam_flag:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


webcam_thread = threading.Thread(target = webcamCap)


app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/start')
def startRender():
    global webcam_flag
    webcam_flag = False
    webcam_thread.run()
    print('[STATUS] Thread running...')

@app.route('/stop')
def stopRender():
    global webcam_flag
    webcam_flag = True
    print('[STATUS] Thread stops...')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)