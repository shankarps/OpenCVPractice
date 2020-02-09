import numpy as np
import cv2 as cv
cap = cv.VideoCapture('./OpenCV/BigBuckBunny.mp4')
print(cap.get(cv.CAP_PROP_FPS))
print(cap.get(cv.CAP_PROP_EXPOSURE))
print(cap.get(cv.CAP_PROP_FRAME_COUNT))
print(cap.get(cv.CAP_PROP_FOURCC))
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
