#Transfer's Diagonal,Determinant in the matrix.0
import numpy as np
n=int(input('n=?'))
a1=np.random.randint(0,10,(5,5))
print(a1)
a2=a1.transpose()
print('tranfers of the matrix\n',a2)
a3=a1.diagonal()
print('Diagonal element of the matrixes\n',a3)
a4=a1.determinant()
print('determinant of the matrix\n',a4)