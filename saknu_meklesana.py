import math

a = int(input("Ievadi koeficientu a: "))
b = int(input("Ievadi koeficientu b: "))
c = int(input("Ievadi koeficientu c: "))

d = b**2-4*a*c # diskriminants
x2 = 0
x1 = 0
if d < 0:
    print ("Vienadojumam nav realu saknu")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("Vienadojumam ir viena sakne: x=", x)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print ("Vienadojumam ir divas saknes: x1 =", x1, " un x2= ", x2)
