# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread(r'images\messi5.jpg', 0)
#
# titles = ['image']
# images = [img]
# for i in range(1):
#     plt.susdbplot(1, 1, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing():
    pass

cv2.namedWindow('thresholds')
img = cv2.imread("lena.jpg", 0)
cv2.createTrackbar('th1', 'thresholds', 100, 250, nothing)
cv2.createTrackbar('th2', 'thresholds', 200, 250, nothing)
th1 = cv2.getTrackbarPos('th1', 'threshold')
th2 = cv2.getTrackbarPos('th2', 'threshold')
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Canny edge detector is an edge detection operator that uses multistage algorithms to
# detect a wide range of edges in images. It was developed by John F. Canny in 1986.

# The Canny edge detection algorithm is composed of 5 steps:
# 1. Noise reduction
# 2. Gradient calculation
# 3. Non-maximum  suppression
# 4. Double threshold
# 5. Edge Tracking by Hysteresis i.e that the finalize the detection of the edges by suppressing
# the edges that are weak or not connected to the main edges.