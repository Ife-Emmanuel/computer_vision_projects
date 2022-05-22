import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'images\lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5)) #blur function is also called average function
gblur = cv2.GaussianBlur(img, (5, 5), 0) # great when dealing with high frequency noise.
median = cv2.medianBlur(img, 5) # this methods replaces each pixel value with the median of its neighbouring pixels. It is good for salt and pepper noise. the kernel size must be odd except 1 because 1 will give the original image.
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75) # Bilateral filter unlike others will not only dissolve the noise but preserve the edges of the image.

# sigma colour is the filter sigma in the colour space
# while the sigma space is the filter sigma in the coordinate space.

titles = ['images', '2D convolution', 'blur', 'gblur', 'median', 'bilateralfilter']
images = [img, dst, blur, gblur, median, bilateralfilter]

for i in range(6):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()