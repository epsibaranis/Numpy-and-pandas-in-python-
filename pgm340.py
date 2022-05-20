# Scalar addition in Series
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
b=np.random.randint(0,100,n)
x1=pd.Series(a)
x2=pd.Series(b)
print('Series x1:',x1)
print('Series x2:',x2)
x3=x1+x2
x4=x1-x2
x5=x1*x2
x6=x1/x2
x7=x1//x2
print('Addition:',x3)
print('Subraction:',x4)
print('Multiplication:',x5)
print('Division:',x6)
print('Floor:',x7)