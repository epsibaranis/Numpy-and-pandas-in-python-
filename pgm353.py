# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:21:56 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
subject=['Tamil','English','Maths','Science','Social Science']
a=np.random.randint(0,100,(20,5))
x=pd.DataFrame(a,columns=subject)
print(x)

