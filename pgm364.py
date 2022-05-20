#data frame
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(20,5))
subject=['Tamil','English','Maths','Science','Social Science']
a1=[i for i in range(10501,10521)]
x=pd.DataFrame(a,columns=subject,index=a1)
print(x)
f=x.drop(index=[10501,10502,10503],axis=0)
print(f)