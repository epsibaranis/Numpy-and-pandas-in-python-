# pandas series
import pandas as pd
n=int(input('n=?'))
d={}

for i in range(n):
 rollno=int(input('rollno=?'))
 name=input('name=?')
 d[rollno]=name
x=pd.Series(d)
print(x)
 