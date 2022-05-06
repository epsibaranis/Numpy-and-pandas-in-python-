# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:15:19 2022

@author: tt
"""
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,10,n)
x=pd.Series(a)
print(x)
x1=x.drop_duplicates()
print(x1)
