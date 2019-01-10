#darbibas ar kopu
from math import sqrt
'''
input_string = input("Ievadi masiva elementus, atdalot tos ar atstarpi: ")
list  = input_string.split()
'''
list = [3, 1, 4, 2, 5]
print("Rekinam masiva elementu vid. aritm.")
count = 0
sum = 0
for num in list:
    count = count + 1
    sum += int (num)
    va = sum/count
print("Vid. aritm. = ",va)

print('Rekinam medianu')
#sakartojam kopu
list.sort()

g = len(list)
#parbaudam atlikumu
if g % 2 == 0:
    d = int(g/2)
    e = int(d+1)
    z = float(list[d-1])
    w = float(list[e-1])
    b = z+w
    me1 = b/2
    print(me1)
    print(d, e, b)
else:
    c = int(g/2+0.5)
    me2 = list[c-1]
    print(me2)

print('Rekinam videjo kvadratisko novirzi')

#vid. aritmetiskais jau aprekinats

#rekina dispersiju
d = g
dissum = 0
while d > 0:
    dis = (float(list[d-1])- va)**2
    dissum = dissum + dis
    d = d - 1

#rekinam vid.kv.novirzi
vidkvn = sqrt(dissum)
print(vidkvn)

print('Sakartojam kopu')
list.sort()
print(list)

print('Kopas mazaka vertiba:', list[0])
print('Kopas lielaka vertiba:', list[g-1])
    






