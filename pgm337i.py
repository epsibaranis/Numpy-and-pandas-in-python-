# print the panda series element by element
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(-100,100,n)
x=pd.Series(a)
print('element by element:')
for i in range(n):
    print(x[i],i,end=',')
print('\n')
print('iteratable object:')
for i in x:
    print(i,end=',')
print('\n')
print('reverse order:')
for i in range(n-1,-1,-1):
    print(x[i],end=',')
print('\n')