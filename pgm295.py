# Generate a n-random numberrs and print  it using numpy

import numpy as np
n=int(input('n=?'))
a=np.random.randint(-100,100,n)
b=set(a)
for i in b:
    m=np.a.count(i)
    print(i,m)