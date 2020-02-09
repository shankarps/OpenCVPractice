import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load a color image in grayscale
img = cv.imread('./media/landscape.jpg', -1)
# print(img)
b, g, r = cv.split(img)
img2 = cv.merge([r, g, b])

plt.subplot(121)
plt.imshow(img)  # expects distorted color
plt.subplot(122)
plt.imshow(img2)  # expect true color
plt.show()
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''

#cv.imwrite('test.png', img)
'''
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
