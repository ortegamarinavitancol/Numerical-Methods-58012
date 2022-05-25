from math import e

def f(x): return e**x

a=-1
b=1
n=21
h=(b-a)/n
S=h*(f(a)+f(b))

for i in range(1,n):
    S=S+f(a+i*h)
Integral=h*S
print('Integral = %f'%Integral)
