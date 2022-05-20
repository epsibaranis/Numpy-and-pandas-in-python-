#load the array
import numpy as np
a1=np.load('pgm333i.py.npy')
for i in a1:
   if i[2]=='Dindigul':
       print(i)