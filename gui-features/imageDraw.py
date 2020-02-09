import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# Draw a diagonal line with thickness of 3 px

#color is RGB
color = (255, 0, 0)
thickness_in_pixels = 2
starting_coordinates = (0, 511)
ending_coordinates = (511, 0)

cv.line(img, starting_coordinates, ending_coordinates,
        color, thickness_in_pixels)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (20, 50), font, 2, (255, 255, 255), 1, cv.LINE_4)
#cv.putText(img, 'OpenCV', (150, 300), font, 2, (0, 0, 255), 1, cv.LINE_4)
cv.rectangle(img, (1, 1), (100, 150), (255, 0, 0), 2)

cv.imwrite('./OpenCV/test.png', img)
plt.imshow(img, interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
