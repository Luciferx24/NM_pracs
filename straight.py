#straight line  curve fitting
#Name : Kaiyyum shakur Dange
#Roll No : 351010  Batch : A1
#AY : 2022-23   Sem : 1
import numpy as np
def pra_slcf(x,y):
  x = x.astype(float)
  y = y.astype(float)
  a = np.array([[len(x),sum(x)],
               [sum(x),sum(x*x)]])
  d = np.array([[sum(y)],
               [sum(x*y)]])
  b = np.linalg.solve(a,d)
  print("y = %.4f + (%.4f) * x"%(b[0],b[1]))

pra_slcf(np.array([6,7,7,8,8,8,9,9,10]),np.array([5,5,4,5,4,3,4,3,3]))