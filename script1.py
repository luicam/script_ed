#!/usr/bin/python
miarray = ['silvia','federico','miguel','julia','evaristo']
print miarray[2]
for elem in miarray:
 print elem, " es un valor contenido en el array miarray"
for index in range(len(miarray)):
   print miarray[index], " es el valor contenido en el array sub ", index
index=0
print "..............................."
for elem in miarray:
   print index, ":", elem
   index += 1
print "..............................."
miarray.append('carlos')
print miarray.index('carlos')
