import cv2
img = cv2.imread('images\lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow('Original image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Pyramid or pyramid representation is a type of multi-scale signal representation in which a signal
# or an image is subject to repeated smoothening and subsampling.


#Gaussian is nothing but repeat filtering and sub-sampling of an image.# There are two functions for gaussian pyramid namely pyrDown and pyrUp
# There are two types of pyramids : 1. Gaussian pyramid
                                #   2. Laplacian pyramid


# There are two functions for gaussian pyramid namely pyrDown and pyrUp

# A level in Laplacian Pyramid is formed by the difference between that level  in the Gaussian pyramid
# and the expanded version of its upper level in Gaussian pyramid.