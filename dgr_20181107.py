#stuff = "Hello\nWorld!"  \n - jauna rinda
#print(stuff)
#print(len(stuff))    parada simbolu skaitu (taja skaita ir ari jauna rinda)

#handle = open("teksts.txt","r") - atver tekstu lasisanai
#print(handle.read()) - parada, kas ir teksta

#xfile = open("teksts.txt")
#for teksts in xfile:
#    print(teksts)

#fhand = open("teksts.txt")
#count = 0
#for line in fhand:
#    count= count+1  skaita rindinu skaitu teksta
#print("Rindas:", count)

#fhand = open("teksts.txt")
#inp = fhand.read() izskaita visus simbolus teksta
#print(len(inp))

#fhand = open("teksts.txt")
#for line in fhand:
#    if line.startswith("teksts"): kriterijs, lai izdukatu konkretas rindas
#        print(line)

#fhand = open("teksts.txt")
#for line in fhand:
#    line = line.rstrip() sis izdzes lieko jauno rindu, ko rada print
#    if line.startswith("teksts"):
#        print(line)

#fhand = open("teksts.txt")
#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith("kakis"):
#        continue
#    print(line)

#fhand = open("teksts.txt")
#for line in fhand:
#    line = line.rstrip()
#    if not "teksts" in line: printe visas rindas kuras ir vards teksts
#        continue
#    print(line)

#fname = raw_input("Ievadi faila nosaukumu: ")
#fhand = open(fname)
#count = 0
#for line in fhand:
#    if line.startswith("teksts"):
#        count = count + 1
#print("Saja", fname, "faila ir", count, "rindas ar vardu teksts")
