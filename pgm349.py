# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:35:15 2022

@author: tt
"""
import pandas as pd
month1=['January','March','May','July','September','November']
rainfall1=[14,15,21,23,25,27]
month2=['February','March','April','July','September','October']
rainfall2=[15,14,23,21,25,31]
x1=pd.Series(rainfall1,month1)
x2=pd.Series(rainfall2,month2)
total=x1+x2
average=(x1+x2)/2
#print(total)
#print(average)
Total1=total.dropna()
Average1=average.dropna()
print(Total1)
print(Average1)
