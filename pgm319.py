# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:27:05 2022

@author: tt
"""

import numpy as np
n=int(input('n=?'))
a1=np.random.randint(0,10,(5,5))
print(a1)
a2=np.sum(a1,axis=0)
print('sum of the column of the matrixes\n',a2)
a3=np.sum(a1,axis=1)
print('sum of the row of the matrixes\n',a3)
a4=np.max(a1,axis=0)
print('max of the column of the matrixes\n',a4)
a5=np.max(a1,axis=1)
print('max of the row of the matrixes\n',a5)
a6=np.min(a1,axis=0)
print('min of the column of the matrixes\n',a6)
a7=np.min(a1,axis=1)
print('min of the row of the matrixes\n',a7)