import sys
sys.path.append("/usr/lib/python2.7/dist-packages/numpy/")
sys.path.append("/usr/lib/python2.7/dist-packages/matplotlib/")
from numpy import sin, linspace
x = linspace(0, 7, 70)
y = sin(x)
y2 = x
y3 = x - ((x**3)/6)
y4 = y3 + ((x**5)/120)
y5 = y4 - ((x**7)/5040)
from matplotlib import pyplot as plt

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin(x)$")
plt.plot(x, y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.show()
