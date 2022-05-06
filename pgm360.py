# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:11:24 2022

@author: tt
"""
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(20,5))
subject=['Tamil','English','Maths','Science','Social Science']
a1=[i for i in range(10501,10521)]
x=pd.DataFrame(a,columns=subject,index=a1)
x['Total']=x['Tamil']+x['English']+x['Maths']+x['Science']+x['Social Science']
print(x)