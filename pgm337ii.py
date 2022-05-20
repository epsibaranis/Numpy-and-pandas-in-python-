import pandas as pd
import numpy as np
n=int(input('n=?'))
a=np.random.randint(-100,100,n)
x=pd.Series(a)
print(x)
print('panda series:\n',x)
print('panda series values:\n',x.values)
print('panda series index:\n',x.index)