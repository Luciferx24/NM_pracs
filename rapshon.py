#Newtons Raphson method 
#Name:Kaiyyum Shakur Dange
#Roll No:351010, Batch:A1
#AY : 2022-23  , Sem : 1

import math as m
def Kaiyyum_nrm(fun,dfun,ddfun,x1,acc,maxitr):

  while  abs(fun(x1)*ddfun(x1)/(dfun(x1))**2)>1:
    print("initial guesses are incorrect, change the initial gueses")
    x1=float(input("enter new x1:"))

  for i in range(maxitr):
    x0=x1-fun(x1)/dfun(x1)

    if abs(x1-x0)<acc:
      break

    else:
      x1=x0

  print("the root of the given function is %.4f"%x0)  

Kaiyyum_nrm(lambda x: m.exp(x)-m.sin(x), lambda x: m.exp(x)-m.cos(x), lambda x: m.exp(x)+m.sin(x),-3,0.00001,10)