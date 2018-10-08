#!/usr/bin/python
# -*- coding: utf-8 -*-

a = input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. pythonā visi input rezultāti ir r str datu tipu
# tāpēc ievadītā lieluma datu tips vēlāk ir jārpārveido
a = int(a)

#pythn valoda balstīta uz C valodas => print strādā līdzīgi printf
# http://www.cplusplus.com/reference/cstdio/printf
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))
