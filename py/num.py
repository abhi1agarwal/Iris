import numpy as np
import matplotlib.pyplot as plt
import sys
import time
a=np.array([(1,2,3),(4,5,6)])
print(a)

S=range(1000)

print(sys.getsizeof(5)*len(S))

D=np.arange(1000)

print(D.size*D.itemsize)

SIZE = 1000000 

start = time.time()
L1 = range(SIZE)
L2= range (SIZE)
result = [x+y for (x,y) in zip(L1,L2)]
print((time.time()-start)*1000)

start = time.time()
A1=np.arange(SIZE)
A2=np.arange(SIZE)
result=A1+A2
print((time.time()-start)*1000)

a=np.array([1,2,3])
print(("%s %d")%("Dimension of 1D numpy array ",a.ndim))
print(a.itemsize)
print(a.dtype)
print(a.shape)
a=np.array([(1,2,3),(4,5,6)])
print(("%s %d")%("Dimension of 2D numpy array ",a.ndim))
print(a.itemsize)
print(a.dtype)
print(a.shape)
a=a.reshape(3,2)
print(a)
a=a.reshape(2,3)
print(a[0:1,2])


a=np.linspace(1,3,10)
print(a)


a=np.array([(1,2,3),(4,5,6)])
print(a.ravel())
print(np.sqrt(a))
print(np.std(a))
print(np.mean(a))


x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()
