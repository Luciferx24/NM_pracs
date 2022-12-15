#curve fitting in power equation : y = alpha * x ^ beta
#Name : Kaiyyum shakur Dange
#Roll No : 351010  Batch : A1
#AY : 2022-23   Sem : 1
import numpy as np
import math  as m
def Kaiyyum_cfpe(x,y):
  x = x.astype(float)
  y = y.astype(float)
  X = np.log(x)
  Y = np.log(y)
  a = np.array([[len(x),sum(X)],
               [sum(X),sum(X * X)]])
  d = np.array([[sum(Y)],
               [sum(X*Y)]])
  b = np.linalg.solve(a,d)
  alpha = np.exp(b[0])
  beta = b[1]
  print("y = %.4f * x ^ %.4f"%(alpha,beta))

Kaiyyum_cfpe(np.array([61,26,7,2.6]), np.array([350,400,50,600]))