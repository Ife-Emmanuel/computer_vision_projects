"""To draw contours on images."""
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\User\PycharmProjects\OpenCVExamples\images\opencv-logo.png')
img = cv2.imread(r'C:\Users\User\Downloads\open_cv_samples\data\rubberwhale1.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(imgray, 127, 255, 0)
# to find contours
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours))


cv2.drawContours(img, contours, -1, (0, 255, 0), 3)




cv2.imshow('image', img)
cv2.imshow('thresh_binary', threshold)
cv2.imshow('gray_image', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

