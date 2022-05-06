# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:38:32 2022

@author: tt
"""
import pandas as pd
month=['January','February','March','April','May','June','July','August','September','October','November','December']
rainfall1=[14,15,21,23,25,27,29,31,33,35,37,39]
x1=pd.Series(rainfall1,month)
print(x1)
rainfall2=[15,14,23,21,25,31,29,35,33,39,37,23]
x2=pd.Series(rainfall2,month)
print(x2)
Total=x1+x2
Average=(x1+x2)/2
print('total of the two series:\n',Total)
print('Average of the two series:\n',Average)