# using unique, nunique, value_counts
import numpy as np
import pandas as pd
n=int(input('n=?'))
a=np.random.randint(0,10,n)
x=pd.Series(a)
print(x)
x1=x.unique()
x2=x.nunique()
x3=x.value_counts()
print('unique value of the series:\n',x1,'\n')
print('No of the unique value in the series:\n',x2,'\n')
print('values count in the series:\n',x3)
