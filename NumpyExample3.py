#Numpy subsetting

import numpy as np

heigth=[1.73,1.68,1.93,1.44]

weigth=[65.2,59.7,63.0,66.9] 

np_heigth=np.array(heigth)
np_weigth=np.array(weigth)

bmi=np_weigth/np_heigth**2

print(bmi)

bmi_23=bmi[bmi>23]
print(bmi_23)
