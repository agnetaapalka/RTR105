# -*- coding: utf-8 -*-
from math import exp

print("y(x)=(1+x)*e^x funkcijas aprēķināšana:")
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = exp(x)*(1+x)
print("y(%0.2f)=(1+%0.2f)*e^%0.2f=%0.2f"%(x,x,x,y),"   /izmantojot bibliotēkas exp f-ju")
print()

def mana_exp_f_ja(x):
   k = 0
   a = ((1+x)*x**k)/(1)
   S = a
   print("a0 = %0.2f S0 = %0.2f"%(a,S))

   while k < 1000:
      k = k + 1
      R = x / k
      a = a * R
      S = S + a
   for k in [999, 1000]:
      print("a%d = %0.2f S%d = %0.2f"%(k,a,k,S))
   return S

yy = mana_exp_f_ja(x)
print("y(%0.2f)=(1+%0.2f)*e^%0.2f caur summu: %0.2f"%(x,x,x,yy))
print()

print('            1000')
print('         _________')
print('         \ ')
print('          \                       k')
print('           \         ( 1 + x ) * x')
print('(1+x)*e^x = >     _____________________ ...,kur -\u221E < x < +\u221E')  
print('           /')
print('          /                 k!')
print('         /________')
print()
print('             k=0')
print()

print('                            x')
print('rekurences reizinātājs:  ________')
print() 
print('                            k')
