import cv2

img = cv2.imread(r'images\WIN_20200409_15_41_09_Pro.jpg')
cv2.imshow('image', img)
h, w, c = img.shape
img1 = cv2.resize(img, (int(w * 0.25), int(h * 0.25)))
cv2.imshow('resizedimage', img1)
cv2.imwrite('imageresized.jpg', img1)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
