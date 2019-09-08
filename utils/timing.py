import numpy as np
import cv2
import os
import configparser


def read(fps, wid, hei, chnl, activBright, deactBright, offset=0):
    cap = cv2.VideoCapture('dod.mp4')
    enabelRead = False

    frame_in_time = 1000.0/fps
    times = []
    i = 0
    lent = 0
    while(cap.isOpened()):
        _, frame = cap.read()  # 150 578<50 - ok
        if frame is None:
            break
        i += 1
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if frame[hei, wid, chnl] < deactBright:
            enabelRead = True
        elif enabelRead and frame[568, 150, 1] > activBright:
            enabelRead = False
            times.append(frame_in_time*i)
            print(times[lent])
            lent += 1
            pass
        # cv2.imshow('frame',gray)
        # if cv2.waitKey(1) or 0xFF == ord('q'):
        #     break

    cap.release()
    cv2.destroyAllWindows()

    with open('times_fw', 'w') as file:  # Use file to refer to the file object
        for time in times:
            file.write(str(time - times[0]+offset))
            file.write("\n")
    pass


def split(st) -> list:
    st = st.replace(" ", "")
    st = st.split(",")
    res = []
    for s in st:
        res.append(int(s))
    return res


if __name__ == "__main__":

    #############CONFIG###############
    path = "utils/config.ini"
    if os.path.exists(path):
        path = "config.ini"

    cof =  configparser.ConfigParser()
    cof.read(path)

    path = cof.get("Settings", "fileName")

    fps = cof.getint("Settings", "frameRate")

    pixelPos = split(cof.get("Settings", "noteShowTime"))

    deactivationBright = cof.getint("Settings", "deactivationBright")

    activationBright = cof.getint("Settings", "activationBright")

    addToFinalTime = cof.getint("Settings", "addToFinalTime")
    #################################


    read(fps, pixelPos[1], pixelPos[0], pixelPos[2],
         activationBright, deactivationBright, addToFinalTime)
