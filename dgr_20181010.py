Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 12.2
>>> y = 14
>>> print(x)
12.2
>>> x = 100
>>> print(x)
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> print(123)
123
>>> print(0982498)
SyntaxError: invalid token
>>> print(0)
0
>>> print(0098098)
SyntaxError: invalid token
>>> print('Hello')
Hello
>>> if = 10
SyntaxError: invalid syntax
>>> if
SyntaxError: invalid syntax
>>> is
SyntaxError: invalid syntax
>>> brak

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    brak
NameError: name 'brak' is not defined
>>> break
SyntaxError: 'break' outside loop
>>> raise

Traceback (most recent call last):
** IDLE Internal Exception: 
  File "/usr/lib/python2.7/idlelib/run.py", line 324, in runcode
    exec code in self.locals
  File "/usr/lib/python2.7/idlelib/run.py", line 112, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "/usr/lib/python2.7/Queue.py", line 176, in get
    raise Empty
Empty
>>> x = 12.2
>>> y = 14
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> type(x)
<type 'int'>
>>> type(y)
<type 'int'>
>>> type(100.)
<type 'float'>
>>> type(a*1.)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(a*1.)
NameError: name 'a' is not defined
>>> a=4
>>> type(a*1)
<type 'int'>
>>> type(a*1.)
<type 'float'>
>>> b=3
>>> c=a%b
>>> c
1
>>> a=4.
>>> c=a%b
>>> c
1.0
>>> a=999
>>> b=1000
>>> c=a % b
>>> c
999
>>> 
