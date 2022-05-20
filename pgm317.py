#Sum, Difference, Product between to arrays
import numpy as np
n=int(input('n=?'))
a1=np.random.randint(0,100,(5,5))
print('first array matrix\n',a1)
a2=np.random.randint(0,100,(5,5))
print('second array matrix\n',a2)
a3=a1+a2
print('sum of two array matrixes\n',a3)
a4=a1-a2
print('Difference of two array matrixes\n',a4)
a5=a1@a2
print('product of two array matrixes\n',a5)