# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:06:54 2022

@author: tt
"""


import numpy as np
import random
n=10
a1=[random.randint(-100,100)for i in range(n)]
a2=np.array(a1,dtype=np.int8)
print('data type of the array',a2.dtype)
print('array',a2)