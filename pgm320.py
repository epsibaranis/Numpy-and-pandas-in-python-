# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:25:39 2022

@author: tt
"""

import numpy as np
a1=np.random.randint(-100,100,(5,5),dtype=np.int8)
print('data type',a1.dtype)
print('random integer array',a1)
a2=np.random.random((5,5))
print(a2.dtype)
print('random real array',a2)