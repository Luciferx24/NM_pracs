import math as m
def func(fun, a, b, n):
    h = (b-a)/n
    y=fun(a)
    yn=fun(b)
    yr=0
    for i in range(1, n-1):
        yr+=fun(a+(i*h))

    ans = (h/2)*((2*yr)+y+yn)
    print(ans)

func(lambda x: 1/(1+x**2), 0, 6, 6)


