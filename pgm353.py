#Data frame with columns
import pandas as pd
import numpy as np
np.random.seed(0)
subject=['Tamil','English','Maths','Science','Social Science']
a=np.random.randint(0,100,(20,5))
x=pd.DataFrame(a,columns=subject)
print(x)