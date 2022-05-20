#print the array and set the data type for the array.
import numpy as np
mynewdatatype=[('Name:',(np.str_,20)),('Age:',np.int8),('Address:',(np.str_,200)),('Email-id:',(np.str_,50)),('Salary:',np.float16)]
d1=('Epsiba Rani S',25,'Soosaiappar street,Kosavapatti','epsibaranis@gmai.com',10000.00)
y=np.array(d1,mynewdatatype)
print(y['Name:'])
print(y['Age:'])
print(y['Address:'])
print(y['Email-id:'])
print(y['Salary:'])