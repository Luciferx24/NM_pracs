#bisection method 
#Name : Kaiyyum Dange
#Roll No : 351010  Batch : A1
#AY : 2022-23   Sem :  1

import math as m

def Kaiyyum_bsm(fun,x1,x2,itr,acc):

  #convergence check
  while fun(x1)*fun(x2)>0:

    print("the roots does not lies in the given range, change the initial guesses")
    x1=float(input("enter the new x1:"))
    x2=float(input("enter the new x2:"))

  #iteration of the roots by using bisection 
  for i in range (1,itr):
      x0=(x1+x2)/2
      if fun(x1)*fun(x0)<0:
        x1=x1
        x2=x0
      elif fun(x1)*fun(x0)>0:
       x1=x0
       x2=x2
      else:
        break;
  
      if abs(x1-x2) <= acc:
       break;
  
  print("the root is",x0)


Kaiyyum_bsm(lambda x: m.cos(x)-1.3*x,0,2,100,0.001)
  
      