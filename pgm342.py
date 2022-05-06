# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:40:31 2022

@author: tt
"""
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
print(x)
x1=x.nlargest()
print('print five first largest number:\n',x1)
x2=x.nsmallest()
print('print five first smallest number:\n',x2)
m=int(input('m=?'))
x3=x.nlargest(m)
print('print m largest number:\n',x3)
x4=x.nsmallest(m)
print('print m smallest number:\n',x4)
