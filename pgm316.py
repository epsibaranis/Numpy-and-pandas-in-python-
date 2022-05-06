# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:05:30 2022

@author: tt
"""

import numpy as np
n=int(input('n=?'))
a1=np.random.randint(0,100,(5,5))
print('array matrix\n',a1)
a2=a1+10
print('addition of array matrix\n',a2)
a3=a1-10
print('subraction of array matrix\n',a3)
a4=a1*10
print('Multiplication of array matrix\n',a4)
a5=a1/10
print('Division of array matrix\n',a5)
a6=a1//10
print('floor of array matrix\n',a6)