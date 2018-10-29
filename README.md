<p align="center">
   <b># RTR105</b><br>
   <b>DATORMĀCĪBAS KURSA ELEKTRONISKĀ KLADE</b><br>

   <b>Pamatkombinācijas</b><br>
  </p>

- ctrl+alt+t - atver termināli
- ctrl+l - notīra simbolus terminālī
- ctrl+shift+t - atver jaunu tabu terminālī

<p align="center">
   <b>2. LEKCIJA</b><br>
   </p>

firefox & - * *palaiž firefox pārlūku* *

**man** + jebkura komanda - * *izprintē komandas iespējas + atslēgas*

uname - * *izprintē operētājsistēmas nosaukumu, versiju un citu info* *

  - lsb_release - * *izprintē specifisko informāciju par OS* *
  
whoami - * *izprintē lietotāja informāciju* *

echo $0 - * *izprintē pašreizējo ''dialektu'' (valodu)* *

pwd - * *izprintē pašreizējo direktoriju (atrašanās vietu)* *

ls - * *izpritnē visus failus un mapes pašreizējā direktorijā* *

ls **-l** - * *izprintē failu tiesības un iespējas jeb detalizētākus sarakstu* *

history - * *izprintē visu vēsturi* *

**PIEMĒRS** - history > history_20180912.txt - * *saglabā vēsturi txt failā* *

<p align="center">
   <b>3. LEKCIJA</b><br>
   </p>

cd - * *maina direktoriju* *

cd . - * *paliek uz vietas direktoijā* *

cd .. - * *pārvieto uz iepriekšējo direktoriju (līmeni augstāk)* *

**~ - * *mājas* ***

mkdir + **nosaukums** - * *izveido jaunu direktoriju* *

rmdir - * *izdzēš direktoriju* *

echo + **'teksts'** - * *izprintē tekstu uz ekrāna līnijā* *

   -  -e \b - * *izdzēš atstarpes* *
   
   -  -e \n - * *pārvieto tekstu jaunā rindā* *
   
 cat - * *atver failu* *
 
 nano - * *atver teksta editoru* *
 
 cp - * *kopē* *
 
 mv - * *pārvieto failu/pārraksta* *
 
 chmod + kods (no bin uz dec) - * *maina faila tiesības* *


<p align="center">
  <b>4. LEKCIJA</b><br>
</p>


PATH - * *izprintē ceļus, kuros meklē skriptus* *

nano ...sh - * *izveido teksta failu ar skriptu* *

PATH=$PATH:... - * *pievieno ceļus patha* *

echo - * *printē uz ekrāna* *

/bin/bash - * *kompilers* *

sudo apt-get - * *lejupielādē papildinājumus* *

git clone (githuba repozitārijas) -  * *izveido mapi ar Githuba repozitāriju* *


<p align="center">
  <b>5. LEKCIJA</b><br>
</p>


*PYTHON*

vars() - * *izprintē funkcijas iespējas* *

__builtins__ - * *izprintē iebūvētās funkcijas* *

__doc__ - * *dokumentē funkciju* *

print (..) - * *izprintē tekstu* *

PYHTON VIDES : 

- python
- idle
- ipython

<p align="center">
<b>6. LEKCIJA</b><br>
</p>


print(...) - * *izprintē rakstīto lietotājam* *

type(..) - * *izprintē datu tipu* *

1. vai a*1.  - * *. pievieno skaitlim datu tipu float* *

integer - * *veselu skaitļu tips* *

string - * *simboli* *

float - * *peldošais tips, daļskaitļi* *



<p align="center">
<b>8. LEKCIJA</b><br>
</p>

Sākot strādāt IDLE, jāatver New file, kurā rakstīt skriptu un ar F5 tas tiek
palaists 

Pēc nosacījuma noteikšanas, jāievieto : 

< - * *mazāks par* *

<= - * *mazāks vai vienāds* *

== - * *vienāds* *

>= - * *lielāks vai vienāds* *

> - * *lielāks* *

!= - * *nav vienāds* *

= - * *piešķiršana* *

range(5) - * *no 0-4* *

if - * *ja* *

for funkcija

elif - * *vai arī (ja papildus nosacījumi)* *

else - * *ja  ne* *


<p align="center">
<b>9. LEKCIJA</b><br>
</p>


  print("%d %d %d"%(one,two,three)) * *- veselu skaitļu interp* *

  %f 			* *- reālu skaitļu interp* *
       
  %s 			* *- simbolu rindas interp* *

3. pythonam - print(greet(),"Gleen")
2. pythonam - greet(),"Gleen"
visiem - print("s% s%"%(greet(),"Gleen"))

def - * *definē savu funkciju* *

PIEMĒRAM - def thing():
            print("Hello")
            
max - * *maksimālā ASCII vērtība tekstam* *

min - * *minimālā ASCII vērtība tekstam* *

i=42 > f=float(i) > print(f) > 42.0 - * *tipa maiņa* *

sval="123" > ival=int(sval) > print(ival + 1) > 124 - * *maina string tipu uz skaitli* *

return - * *atgriežās ar izpildītu funkciju un rezultātu* *

def addtwo(a,b): added=a+b return added > x=addtwo(3, 5) print(x) > 8 * *vairāki parametri* *


<p align="center">
<b>10. LEKCIJA</b><br>
</p>

<p align="center">
<b>CIKLI</b><br>
</p>

n=5

while n>0:

  print(n)

  n=n-1

print("Blastoff!")

print(n)

---------------------------------------------------------------------------------------

n = 5            * *nebeidzams cikls* *

while n > 0 :

   print('Lather')

   print('Rinse')

print('Dry off!')



---------------------------------------------------------------------------------------



while True:              * *cikla pārtraukšana* *

line = input('> ')

  if line == 'done' :

  break (pārtrauc ciklu vispārīgi)

 print(line)

print('Done!')

---------------------------------------------------------------------------------------

while True:               * *turpināšanas cikls* *

line = input('> ')

if line[0] == '#' :

continue (neizbeidz ciklu, atgriežas pie nosacījuma)

if line == 'done' :

break

print(line)

print('Done!')


---------------------------------------------------------------------------------------

for i in [5, 4, 3, 2, 1] : - * *definēts cikls* *

print(i)

print('Blastoff!')


---------------------------------------------------------------------------------------


friends = ['Joseph', 'Glenn', 'Sally'] - * *definēts cikls ar simboliem* *

for friend in friends :

print('Happy New Year:', friend)

print('Done!')


---------------------------------------------------------------------------------------


largest_so_far = -1 - * *meklē lielāko vērtību* *

print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15] :

if the_num > largest_so_far :

largest_so_far = the_num

print(largest_so_far, the_num)

print('After', largest_so_far)

---------------------------------------------------------------------------------------


zork = 0 - * *skaitīšana ciklā* *

print('Before', zork)

for thing in [9, 41, 12, 3, 74, 15] :

zork = zork + 1

print(zork, thing)

print('After', zork)


---------------------------------------------------------------------------------------
zork = 0 - * *saskatīšana ciklā* *

print('Before', zork)

for thing in [9, 41, 12, 3, 74, 15] :

zork = zork + thing

print(zork, thing)

print('After', zork)


---------------------------------------------------------------------------------------

count = 0 - * *vidējās vērtības meklēšana* *

sum = 0

print('Before', count, sum)

for value in [9, 41, 12, 3, 74, 15] :

count = count + 1

sum = sum + value

print(count, sum, value)

print('After', count, sum, sum / count)



print('Before') - * *filtrēšna ciklā* *

for value in [9, 41, 12, 3, 74, 15] :

if value > 20:

print('Large number',value)

print('After')


