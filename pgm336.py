# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:27:46 2022

@author: tt
"""
import numpy as np
a1=np.load('pgm333i.py.npy')
for i in a1:
   if i[2]=='Dindigul':
       print(i)