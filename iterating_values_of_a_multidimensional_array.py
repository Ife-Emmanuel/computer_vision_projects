# c = 3
# r = 3
# arr = [[0] * c for i in range(r)]
# # loop will run for the length of the inner lists
# # loop will run for the length of the outer list
# for i in range(r):
#      for j in range(c):
#          if i < j:
#              arr[i][j] = 8
#          elif i > j:
#              arr[i][j] = 4
#          else:
#              arr[i][j] = 7
#          # for r in arr:
#          #     print(' '.join([str(x) for x in arr]))
# #print([r for r in arr])
# print(' '.join([str(x) for x in arr]))

# Creating a Numpy Array
# import numpy as np
# # Array of integers.
# x = np.array([[1, 6, 7], [5, 9, 2]])
# print(x)
#
# print('\n=======================================\n')
# # Array of floats
# x = np.array([[1, 6.2, 7], [5, 9, 2]])
# print(x)
#
# print('\n====================================================\n')
# # Array of complex numbers
# x = np.array([[1, 6, 7], [5, 9, 2]], dtype= complex)
# print(x)
# # The thing is numpy is very good for mathematical calculations and especially with arrays also.
# print('X' * 30)
#
# # Accessing Numpy Matrix Elements, Rows and Columns
# x = np.array([[[1, 6], [7, 8], [1, 9]], [[5, 9], [2, 3], [2, 0]], [[3, 8], [4, 5], [1, 3]]])
# print(x[1][2])
# print('\n' + str(x[0]))
# print('\n' + str(x[1]))
# print('\n' + str(x[-1]))
# print('===================================================\n')
# print(x[ :, :, -1])
#
# #Wow mathematics and numpy is fucking interesting.
# for list in x[ :, :, 0]:
#     for number in list:
#         print(number)

#What if it is not a numpy array?
import array
# print('=================================')
# x = [[1, 2, 4], [3, 1, 0], [2, 2, 8]]
# x = array.array['i', x]
# #x = np.array(x)
# print(x[ :, 0])

# import cv2
# #img = np.ones((512, 512, 3), np.uint8)
# img = cv2.imread(r'images\lena.jpg')
# #img = img[: 256]
# img1 = np.ones((512, 512, 3), np.uint8)
# img = img[ : ]
# print(img)
# print('=====================================')
# print(img1)
# # img1[ :, :, 0] = 255
# # img1[ :, :, 1] = 255
# # img1[:, :, 2] = 255
# print(img.size)
# print(img.shape)
# cv2.imshow('image', img)
# cv2.imshow('image1', img1)
#
# cv2.waitKey(0)

#Some Properties of Numpy Array
import numpy as np
import cv2
zero_array = np.zeros((3, 2))
cv2.imshow('zero_image', zero_array)
print('zero_array = ', zero_array)
one_array = np.ones((3, 2))
cv2.imshow('ones_image', one_array)
print('\n111111111111111111111111111111111\n')
print('one_array = ', one_array)
x = np.arange(16).reshape(4, 4)
print('\n===============================\n')
print('x = ', x)
cv2.waitKey(0)

#print('Transpose of x ', x.transpose())

# explaina