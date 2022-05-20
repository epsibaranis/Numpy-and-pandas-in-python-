# count of the positive number, negative number,zeroes number.
import numpy as np
a2=np.loadtxt('pgm321.py')
x=0
y=0
z=0
for i in a2:
    if i>0:
        x=x+1
    elif i<0:
        y=y+1
    else:
        z=z+1
print('count of the positive number',x)
print('count of the negative number',y)
print('count of the zeroes number',z)