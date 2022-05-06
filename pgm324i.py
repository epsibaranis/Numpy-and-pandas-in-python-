# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:52:18 2022

@author: tt
"""
import numpy as np
a1=np.loadtxt('pgm324.py')
print(a1)
a2=np.max(a1,axis=0)
print('Biggest element of the rows',a2)
a3=np.max(a1,axis=1)
print('Biggest element of the coloumn',a3)
a4=np.min(a1,axis=0)
print('smallest element of the rows',a4)
a5=np.min(a1,axis=1)
print('smallest element of the coloumn',a5)
