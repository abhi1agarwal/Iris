import random 
import sys
import os

print("Hello World")

name = "Abhinandan"
 
print(name)
#five main datatypes overall 
'''
Numbers, strings, Lists, Tuples, Distionaries
'''
name = 15

print(name)

print((5.0/4))
print((5//2))
#assad
yahu = ''' Come crawling faster
Obey your master
'''
print("%s %s" % ( 'And he said', yahu ) )
print("yo"*5)

print('asdsa','asdsad')
gl=['yahu','bahu']
print('First Item',gl[0])
gl[0]="tahu"
print('First Item',gl[0])
gl.append("hahappendedhuh!")
print(gl)
gl.insert(0,"isntthisthenewfirstelement?")
print(gl)
gl.remove("bahu")
print("\nLooking for removal...")
print(gl)
gl.insert(2,"bahu") #inserted back 
gl.remove(gl[2])
print("\nLooking for removal method 2...")
print(gl)
gl.sort()
gl.reverse()
print(gl)

gl.insert(2,"bahu")
print(gl)
del gl[2]
print(gl)
a=len(gl)
print(a)
print(a*2)

print(min(gl))
print(max(gl))

