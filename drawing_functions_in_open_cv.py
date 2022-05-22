import numpy
import cv2

img = cv2.imread('resized.png', 1)
img = cv2.line(img, (0, 140), (140, 140), (147, 96, 44), 5)
img = cv2.arrowedLine(img, (0, 0), (140, 140), (255, 0, 0), 5)
img = cv2.rectangle(img, (154, 0), (254, 80), (0, 0, 255), 10)
img = cv2.circle(img, (204, 40), 35, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (3, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()