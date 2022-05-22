#array = [ [[0] * 4] * 3]
array = [[0] * 4] * 3
print(array)
# What I notice in essence is that you dont have to be putting the multipled list itself in bracket again.
# array[0][0][0] = 5
# print(array)

c = 4
r = 3
print('\n ==========================================')
array = [ [0] * c for i in range(r)]
print(array)
array[0][0] = 5
print('\n============================================')
print(array)

import numpy as np
one_array = np.ones((3, 2))
print('one_array = ', one_array)
x = np.arange(9).reshape(3, 3)
print('x = ', x)
print('Transpose of x ', x.transpose())