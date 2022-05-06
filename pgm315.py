# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:38:30 2022

@author: tt
"""

import numpy as np
n=int(input('n=?'))
a1=np.random.randint(0,10,(5,5))
print(a1)
j1=a1[0:1,0:3]
print('first row\'s first three values',j1)
j2=a1[0:1,2:5]
print('first row\'s last three values',j2)
j3=a1[1:2,1:4]
print('second row\'s middle three value',j3)
j4=a1[2:4,1:4]
print('third & fourth rows middle three value\n',j4)
j5=a1[3:5,0:3]
print('fourth & fivth row\'s first three value\n',j5)