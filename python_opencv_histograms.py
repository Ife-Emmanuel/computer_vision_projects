import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# img = cv.imread(r'images\lena.jpg', 1)
# b, g, r = cv.split(img)
# hist = cv.calcHist(img, [0], None, [256], [0, 256])
# plt.plot(hist)
# print('\nBlue', b.ravel())
# print('\nGreen\n', g.ravel())
# print('               \nRed\n', r.ravel())
# img = np.zeros((200, 200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#
# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)
#
# # to draw the histogram for bgr image
# # Histogram is a graph that gives you an overall idea about the intensity distribution of an image.
# # plt.hist(b.ravel(), 256, [0, 256])
# # plt.hist(g.ravel(), 256, [0, 256])
# # plt.hist(r.ravel(), 256, [0, 256])
#
#
# titles = ['blue', 'green', 'red']
# colours = [b, g, r]
#
# for i in range(3):
#     plt.hist(colours[i].ravel(), 256, [0, 256])
#     #plt.title(titles[i])
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()


# It is highly an opportunity to invest in before it gets too late
# programming can take you far in life if you are very serious with i
a = np.array([0, 2, 8, 8, 7, 3, 1, 4, 3])
plt.hist(a, 8, [0, 7])
plt.show()