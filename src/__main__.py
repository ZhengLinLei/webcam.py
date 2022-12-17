# AUTHOR: ZLL
# https://github.com/ZhengLinLei
#
# Apache 2.0

import cv2

# GET VIDEO, 0 PARAM FOR EXTERNAL CAMERA
video = cv2.VideoCapture(0)


playCamera = True # START SHOWING THE CAMERA
WNTITLE = 'WebCam'


while playCamera:
    # GET DATA
    check, frame = video.read()

    if check:
        # SHOW THE VIDEO

        cv2.imshow(WNTITLE, frame) 

        # GET KEY
        key = cv2.waitKey(1)

        if key == 27 or cv2.getWindowProperty(WNTITLE, cv2.WND_PROP_VISIBLE) < 1: # ESC KEY CODE OR x
            playCamera = False

            break
    else:
        print('Cannot get information about your webcam device')
        playCamera = False



# SHUTDOWN THE CAMERA AND KILL THE PROCCESS WHEN THE USER CLOSE THE PROCCESS
# THIS HELP TO KILL THE PROCCESS USING THE CAMERA
# 
#
video.release()

cv2.destroyAllWindows()