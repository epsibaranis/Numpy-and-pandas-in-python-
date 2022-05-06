# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:22:03 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.DataFrame(a)
print(x)
