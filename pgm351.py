#Data Frame
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(3,3))
x=pd.DataFrame(a)
print(x)
