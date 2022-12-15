#Runge-Kutta method
#Name : Kaiyyum Shakur Dange
#Roll No: 351010   Batch : A1
#AY : 2022-23    Sem - 1
import math as m
def Kaiyyum_RK2(fun,x0,y0,xn,n):
  h = (xn-x0)/n
  yi = y0
  xi = x0
  for i in range(1,n+1):
    k1 = h*fun(xi,yi)
    k2 = h*fun(xi + h,yi + k1)
    yi = yi + 1/2 *(k1 + k2)
    xi = xi + h
    print("x= %.4f"%xi,"y = %.4f"%yi)

Kaiyyum_RK2(lambda x,y: y + m.exp(x),0,0,0.3,3)