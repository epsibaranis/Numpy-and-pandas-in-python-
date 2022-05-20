# Data Frame
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(20,5))
x=pd.DataFrame(a)
print(x)