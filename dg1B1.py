Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path.append("/usr/lib/python2.7/dist-packages/numpy/")
>>> from numpy import *
>>> x = linspace(0, 7, 70)
>>> y = cos(x)
