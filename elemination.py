#Gauss Elimination method
#Name:Kaiyyum Shakur Dange
#Roll No:351010, Batch:A1
#AY : 2022-23  , Sem : 1

import numpy as np
def Kaiyyum_gem(a,d):
  a = np.array(a, dtype = float)
  d = np.array(d, dtype = float)
  n = len(d)
  print("Number of equations = ",n)
  for i in range(0,n,1):
    for k in range (i+1,n,1):
      fact = a[k,i]/a[i,i]
      for j in range(0,n,1):
        a[k,j] = a[k,j] - fact*a[i,j]
        d[k] = d[k] - fact*d[i]
  print("Upper Triangular Matrix =")
  print(a)
  print(d)
  x = np.zeros(n)
  for i in range(n-1,-1,-1):
    temp = 0
    for j in range(i+1,n,1):
      temp = temp + a[i,j]*x[j]
    x[i] = (d[i]-temp)/a[i,i]
  for i in range(n):
       print("x(%i) = %.4f"%(i,x[i]))

Kaiyyum_gem(np.array([[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]]), np.array([40,40,40,40]))