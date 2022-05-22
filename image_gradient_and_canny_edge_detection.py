import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'messi5.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize= 3)
lap = np.uint8(np.absolute(lap)) # it convert the absolute value returned from previous line of code to 8 bits integers we can work with.
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)


sobelx = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobelY))
sobelcombined = cv2.bitwise_or(sobelx, sobely)
edges = cv2.Canny(img, 100, 200)
print('\nedges\n', edges)




titles = ['image', 'laplacian', 'sobelx', 'sobely', 'sobelcombined', 'Canny']
images = [img, lap, sobelx, sobely, sobelcombined, edges]
for i in range(6):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()