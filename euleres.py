#Eulers Method
#Name : Kaiyyum Shakur Dange
#Roll No. 351010
#Batch : A1
#AY : 2022-23 Sem : 1

import math as m
def Kaiyyum_EM(fun,x0,y0,xn,n):
  h = (xn - x0)/n
  yi = y0
  xi  = x0
  for i in range(1,n+1):
    yi = yi + h*fun(xi,yi)
    xi = xi +h
    print("x = %.4f"%xi,"y = %.4f"%yi)

Kaiyyum_EM(lambda x,y : x+y,0,1,1,5)