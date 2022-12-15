import numpy as np
a = np.array([[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]])
d = np.array([40,40,40,40])
a = np.array(a, dtype = float)
d = np.array(d, dtype = float)
n = len(d)
maxitr = 6
print("Number of equations = ",n)
x = np.zeros(n)
for itr in range(maxitr):
    for i in range(0,n,1):
      temp = 0
      for j in range(0,n,1):
        if (i!=j):
          temp = temp + a[i,j]*x[j]
      x[i] = (d[i]-temp)/a[i,i]
for i in range(0,n,1):
  print(x[i])