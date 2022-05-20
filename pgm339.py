# vector addition in Series
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
print('Series:',x)
x1=x+10
print('Addition:',x1)
x2=x-10
print('Subraction:',x2)
x3=x*10
print('Multiplication:',x3)
x4=x/10
print('Division:',x4)
x5=x//10
print('Floor:',x5)