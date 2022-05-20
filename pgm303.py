# Addition, subraction,multiplication,division, floor on two numpy arrays.
import numpy as np
import random
random.seed(0)
n=int(input('n=?'))
a=[random.randint(-100,100)for i in range(n)]
b=[random.randint(-100,100)for i in range(n)]
n1=np.array(a)
n2=np.array(b)
c1=n1+n2
c2=n1-n2
c3=n1*n2
c4=n1/n2
c5=n1//n2
print('n1  arrary:',n1)
print('n2  arrary:',n2,'\n')
print('Addition of two arrays:      n1+n2=',c1,'\n')
print('subraction of two arrays:    n1-n2=',c2,'\n')
print('multiplication of two arrays:n1*n2=',c3,'\n')
print('Division of two arrays:      n1/n2=',c4,'\n')
print('floor of two arrays:        n1//n2=',c5)