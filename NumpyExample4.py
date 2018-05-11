#Numpy 2-D array

import numpy as np

np_2d=np.array([[1.73,1.68,1.93,1.44],
		[65.2,59.7,63.0,66.9]])

print(np_2d)

print(np_2d.shape)

print(np_2d[0][2])

print(np_2d[0,2])

print(np_2d[:,1:3])

print(np_2d[1:])
