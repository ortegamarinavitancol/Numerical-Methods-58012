from math import sin

def f(x): return sin(x*3)

a=0
b=0.6
n=7
h=(b-a)/n
S=h*(f(a)+f(b))

for i in range(1,n):
    S=S+f(a+i*h)
Integral=h*S
print('Integral = %f'%Integral)