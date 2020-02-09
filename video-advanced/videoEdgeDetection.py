import argparse
import cv2 as cv
import numpy as np


def capture_stream():
    # Init video
    capture = cv.VideoCapture('C:/media/BigBuckBunny.mp4')
    out = cv.VideoWriter('C:/media/out.mp4', 0x00000021, 30, (100,  100))
    # Get and open video capture
    while capture.isOpened():
        # Re-size the frame to 100x100
        ret, frame = capture.read()
        if not ret:
            break
        # print(frame.shape)
        frame = cv.resize(frame, (100, 100))
        # Add Canny Edge Detection to the frame,
        # with min & max values of 100 and 200
        # use np.dstack after to make a 3-channel image
        frame = cv.Canny(frame, 100, 200)
        frame = np.dstack((frame, frame, frame))
        # Write out the frame
        out.write(frame)
    # Close the stream and windows
    out.release()
    capture.release()
    cv.destroyAllWindows()


def main():
    capture_stream()


if __name__ == "__main__":
    main()
