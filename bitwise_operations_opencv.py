import cv2
import numpy as np

#masks are binary images that indicate the pixel in which a operation is to performed.

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img, (250, 0), (500, 250), (255, 255, 255), -1)

#bitAnd = cv2.bitwise_and(img2, img1)
#bitor = cv2.bitwise_or(img2, img1)
#bitxor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitor', bitor)
#cv2.imshow('bitxor', bitxor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()