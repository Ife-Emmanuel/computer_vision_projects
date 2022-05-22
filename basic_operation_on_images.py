import numpy as np
import cv2

img = cv2.imread(r'images\messi5.jpg')
img2 = cv2.imread(r'images\opencv-logo-white.png')

print(img.shape) #returns a tuple of number of rows, columns and channels
print(img.size) #returns total number of pixels is accessed
print(img.dtype) #returns image datatype is obtained

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280 : 340, 330: 390]
img[273 : 333, 100 : 160] = ball
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
print('gray_image ', imggray.shape)
cv2.imshow('unresized_image', img)
cv2.imshow('grayimage', imggray)
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# dst = cv2.add(img, img2)

cv2.imshow('image', img)
dst = cv2.addWeighted(img, .8, img2, .2, 0)
cv2.imwrite('added_image.jpg', dst)
cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()