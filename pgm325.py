# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:19:18 2022

@author: tt
"""
import numpy as np
mynewdatatype=[('Name:',(np.str_,20)),('Age:',np.int8),('Address:',(np.str_,200)),('Email-id:',(np.str_,50)),('Salary:',np.float16)]
d1=('Epsiba Rani S',25,'Soosaiappar street,Kosavapatti','epsibaranis@gmai.com',10000.00)
y=np.array(d1,mynewdatatype)
print(y['Name:'])
print(y['Age:'])
print(y['Address:'])
print(y['Email-id:'])
print(y['Salary:'])
