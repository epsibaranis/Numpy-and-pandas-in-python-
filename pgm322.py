# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:33:51 2022

@author: tt
"""
import numpy as np
n=int(input('n=?'))
a1=np.random.randint(-100,100,(n,n),dtype=np.int8)
print(a1)
np.savetxt('pgm324.py',a1)
