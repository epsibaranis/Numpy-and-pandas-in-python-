# save the array in txt
import numpy as np
n=int(input('n=?'))
a1=np.random.randint(-100,100,(n,n),dtype=np.int8)
print(a1)
np.savetxt('pgm324.py',a1)
