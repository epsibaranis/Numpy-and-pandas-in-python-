# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:42:55 2022

@author: tt
"""
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
print('series:',x)
x1=x.sum()
x2=x.max()
x3=x.min()
x4=x.product()
x5=x.mean()
print('sum:\n',x1)
print('max:\n',x2)
print('min:\n',x3)
print('product:\n',x4)
print('mean:\n',x5)


