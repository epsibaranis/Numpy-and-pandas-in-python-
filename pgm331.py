# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:36:29 2022

@author: tt
"""
import numpy as np
mynewdtype=[('Name:',(np.str_,20)),('Age:',np.int8),('Address:',(np.str_,200)),('Email-id:',(np.str_,50)),('Salary:',np.float16)]
n=int(input('n=?'))
a1=np.zeros(n,mynewdtype)
for i in range(n):
    n1=input('Name:')
    n2=int(input('Age:'))
    n3=input('Address:')
    n4=input('Email-id:')
    n5=float(input('Salary:'))
    d1=(n1,n2,n3,n4,n5)
    a1[i]=d1
print(a1)
np.save('pgm333i.py',a1)
