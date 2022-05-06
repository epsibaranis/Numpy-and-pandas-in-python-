# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:52:12 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(20,5))
x=pd.DataFrame(a)
print(x)
