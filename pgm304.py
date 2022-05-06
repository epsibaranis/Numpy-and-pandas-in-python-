# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:38:37 2022

@author: tt
"""
#pgm 304
import numpy as np
import random
random.seed(0)
n=int(input('n=?'))
a=[random.randint(-100,100)for i in range(n)]
b=np.array(a)
c1=np.sum(b)
c2=np.max(b)
c3=np.min(b)
c4=np.unique(b)
c5=np.unique(b,return_index=True)
c6=np.unique(b,return_counts=True)
c7=np.flip(b)
print('b array:',b)
print('sum of  the elements  in a  array:','','','','','','',c1,'\n')
print('max of  the elements in  a  array:','','','','','','',c2,'\n')
print('min of  the elements  in a  array:','','','','','','',c3,'\n')
print('unique of the elements in a array:','','','','','','','',c4,'\n')
print('unique values index  of the elements in a array :',c5[1],'\n')
print('unique values counts of the elements in a array :',c6[1],'\n')
print('flip   of the elements in a array:','','','','','','',c7,'\n')