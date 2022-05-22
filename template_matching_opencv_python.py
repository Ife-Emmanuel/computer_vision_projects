import cv2
import numpy as np
img = cv2.imread(r'images\messi5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r'messi_face/.jpg', 0)

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.8;
loc = np.where(res >= threshold)
print(loc)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()