# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:38:55 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(3,3))
x=pd.DataFrame(a)
print(x)
