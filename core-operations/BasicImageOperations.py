import numpy as np
import cv2 as cv
import os

img = cv.imread('./media/landscape.jpg')

# get one pixel in BGR mode
px = img[100, 100]
print(px)

# accessing RED value of a pixel
red = img.item(100, 100, 2)
print(red)

# image shape - rows, columns and color channels
print(img.shape)

# total number of pixels
print(img.size)

# Adding a rectangle in the image.
cv.rectangle(img, (1, 300), (100, 350), (255, 0, 0), 2)

segment = img[1:120, 1:100]
img[301:420, 501:600] = segment

#reflect = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REFLECT)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
