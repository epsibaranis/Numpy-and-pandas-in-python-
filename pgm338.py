# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:25:52 2022

@author: tt
"""
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
a1=x[::]
print('print the entire array:\n',a1)
a2=x[::-1]
print('print the array in the reverse array:\n',a2)
a3=x[:5]
print('print first five element:\n',a3)
a4=x[:5:-1]
print('print five element in the reverse order:\n',a4)
a5=x[5:]
print('print 5th position to all the element to array:\n',a5)
a6=x[-5:]
print('print the element from index-5 to end of the array:\n',a6)
a7=x[5:-5]
print('print the element from index 5 to index-5:\n',a7)
a8=x[::2]
print('print the entire array with forward indexing with step2:\n',a8)
a9=x[::-2]
print('print the entire array in the reverse order with step2:\n',a9)

