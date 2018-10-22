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


print("%d %d %d"%(one,two,three)) - veselu skaitļu interpretācija
       %f %f %f				       - reālu skaitļu interpretācija
       %s %s %s				       - simbolu rindas interpretācija


3. pythonam - print(greet(),"Gleen")
2. pythonam - greet(),"Gleen"
visiem - print("s% s%"%(greet(),"Gleen"))
