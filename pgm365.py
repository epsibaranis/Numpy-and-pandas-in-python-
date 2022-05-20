# data frame
import pandas as pd
import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,(20,5))
subject=['Tamil','English','Maths','Science','Social Science']
a1=[i for i in range(10501,10521)]
x=pd.DataFrame(a,columns=subject,index=a1)
j1=x.loc[10501:10521,'Tamil':'Social Science']
j2=x.loc[10501:10502,'Tamil':'Maths']
j3=x.loc[10502:10503,'English':'Science']
j4=x.loc[10503:10505,'English':'Science']
j5=x.loc[10504:10506,'Tamil':'Maths']
print(j1)
print(j2)
print(j3)
print(j4)
print(j5)