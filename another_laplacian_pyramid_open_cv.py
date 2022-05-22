import cv2
import numpy as np
img = cv2.imread(r'images\lena.jpg')
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

# Now for the laplacian pyramid
# Hence laplacian pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()

# laplacian and gaussian images helps to blend images and reconstruct images.
