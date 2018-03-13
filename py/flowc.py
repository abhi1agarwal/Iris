import random 
import sys
import os

#  if else elif


age = 21
if age>16 :
	print('You are old enough to drive')
else : 
	print('You are not old enough bruh!')


for x in range(0,10):
	print(x , ' ' , end = "" )
print('')

sup = ['superman','spiderman','ironman','blackpanther']

for x in sup:
	print(x, 'is superhot')

for x in [0,2]:
	print(sup[x], ' is my fav')


#Watch out the differences between
viola=range(1,10)
print(viola[2])
print(viola)
#and
viola=list(range(1,10))
print(viola[2])
print(viola)
# ---- 


rakh=random.randrange(0,100)
print(rakh)
while (rakh != 15):
	print(rakh)
	rakh=random.randrange(0,100)

print('finally ',rakh)