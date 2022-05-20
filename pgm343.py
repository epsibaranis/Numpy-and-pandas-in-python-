#using drop_duplicates function in Series
import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(0,10,n)
x=pd.Series(a)
print(x)
x1=x.drop_duplicates()
print(x1)