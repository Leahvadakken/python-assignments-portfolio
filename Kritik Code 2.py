import numpy as np
np.seterr(divide='ignore')
def roots(f,a,b):
    tol=10**-10
    while abs(a-b)>10**-10:
        m = ((b+a)/2)
        if f(a)<=0<=f(b) or f(b)<=0<=f(a):
            if f(a) == 0:
                return a
            elif f(b)==0:
                return b
            elif f(m) == 0:
                return m

            if (f(a)<=0<=f(m)) or (f(m)<=0<=f(a)):
                b=m

            elif (f(m)<=0<=f(b)) or (f(b)<=0<=f(m)):
                a=m

        else:
            return "root not in range [a,b]"
    return round(m, 10)
def f(x):
    return np.exp(x) + np.log(x)
print(roots(f,0,1))
def a(x):
    return np.arctan(x) - ((x)**2)
print (f"{roots(a,0,2):.10f}")

def b(x):
    return (np.sin(x))/(np.log(x))
print (roots(b,3,4))

def c(x):
    return np.log(np.cos(x))
print (roots(c,5,7))

