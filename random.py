from numpy import random as r
x = r.uniform(0,10,10)
print(x)

y = r.normal(0,1,5)
print(y)

r.seed(3)
t = r.random()
print(t)
r.seed(3)
t = r.random()
print(t)
