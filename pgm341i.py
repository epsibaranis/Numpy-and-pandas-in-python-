# Using Describe functions in Series
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.Series(a)
print('series:',x)
x1=x.describe()
print(x1)