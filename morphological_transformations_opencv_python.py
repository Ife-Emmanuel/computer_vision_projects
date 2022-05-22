import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'images\smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations= 2)
erosion = cv2.erode(mask, kernal, iterations= 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#morphological transformations are some simple operations based on
# image shape.
# it is normally performed on a binary images Two things are required which are the original
# image and the structure or kernel which decides

#dilation
# By the time we apply the kernel, the pixel element is one if at least one pixel under
# the kernel is one

# erosion
# by the time we apply the kernel, the pixel element is one only if all pixels under the
#kernal is one.

# tophat
# it is the difference between the image and opening of an image

# morphological gradient
# it is the difference between the dilation and erosion of an
# image.