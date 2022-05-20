# Data frame
import pandas as pd
import numpy as np
np.random.seed(0)
n=int(input('n=?'))
a=np.random.randint(0,100,n)
x=pd.DataFrame(a)
print(x)
