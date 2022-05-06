# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:13:39 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
subject=['Tamil','English','Maths','Science','Social Science']
a=np.random.randint(0,100,(20,5))
a1=[i for i in range(10501,10521)]
x=pd.DataFrame(a,columns=subject,index=a1)
y1=x.head()
y2=x.tail()
n=int(input('n=?'))
y3=x.head(n)
y4=x.tail(n)
print('head of the first 5 element of the dataframe:\n',y1)
print('tail of the first 5 element of the dataframe:\n',y2)
print('head of the n element of the dataframe:\n',y3)
print('tail of the n element of the dataframe:\n',y4)
y5=x.describe()
print('describe of the dataframe:\n',y5)
