# Head and Tail functions in python
import pandas as pd
import numpy as np
n=int(input('n=?'))
n1=int(input('n1=?'))
a=np.random.randint(-100,100,n1)
x=pd.Series(a)
print(x)
y1=x.head()
y2=x.tail()
print(y1)
print(y2)
y3=x.head(n)
y4=x.tail(n)
print(y3)
print(y4)