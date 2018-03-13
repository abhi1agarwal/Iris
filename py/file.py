import random 
import sys
import os

tf=open('test.txt','wb')
print(tf)
print(tf.mode)
print(tf.name)
print("hugo\n")
# print(bytes("hugo\n",'UTF-8'))
tf.write(bytes("hugo\n",'UTF-8'))
tf.write(bytes("bugo\n",'UTF-8'))
tf.write(bytes("tugo\n",'UTF-8'))
# tf.write("hugo\n") # Wont work this way

#finally, to close, use close.
tf.close()

tf=open('test.txt','r+')
print(tf.mode)
wegot=tf.read()
print(wegot)

print("Enter any number ::")
yo=sys.stdin.readline()
print("read :: ",yo.strip())
print("remains :: ",yo)
print(int(yo)*2)

