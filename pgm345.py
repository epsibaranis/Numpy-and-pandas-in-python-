# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:26:36 2022

@author: tt
"""
import numpy as np
import pandas as pd
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
print(x)
x1=x.sort_values()
print('Sorting the series based values:\n',x1,'\n')
x2=x.sort_values(ascending=False)
print('Decending values sorting the series based values:\n',x2,'\n')
x3=x.sort_index()
print('sorting the series based index:\n',x3,'\n')
x4=x.sort_index(ascending=False)
print('decending values sorting the series based index:\n',x4,'\n')
